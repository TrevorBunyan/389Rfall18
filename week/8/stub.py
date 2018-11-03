#!/usr/bin/env python2

import sys
import struct
import datetime



# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
offset = 8

timestamp = struct.unpack("<L", data[offset:offset + 4])[0]
offset += 4
UTCtimestamp = datetime.datetime.fromtimestamp(timestamp)
print("TIMESTAMP: " + UTCtimestamp.__str__())

author = struct.unpack("<8s", data[offset:offset + 8])[0]
offset += 8
print("AUTHOR: " + author)

section_count = struct.unpack("<L", data[offset:offset + 4])[0]
offset += 4
print("SECTION COUNT: %d" % int(section_count))

print("-------  BODY  -------")

for count in range(section_count + 2):
    section_type = hex(struct.unpack("<L", data[offset:offset + 4])[0])
    offset += 4
    section_length = int(struct.unpack("<L", data[offset:offset + 4])[0])
    offset += 4

    if section_type == "0x1":  # SECTION_PNG
        print("PNG:")

        png_contents = struct.unpack("<%ds" %section_length, data[offset:offset + section_length])[0]
        f = open(author + "_fpff.png", "w")
        f.write(png_contents)
        f.close()
        print("Generated file in the current directory.")
    elif section_type == "0x2":  # SECTION_DWORDS
        print("DWORDS:")
        dwords = struct.unpack("<%dq" %(section_length / 8), data[offset:offset + section_length])
        print(dwords)
    elif section_type == "0x3":   # SECTION_UTF8
        utf_text = struct.unpack("<%ds" % section_length, data[offset:offset + section_length])[0]
        print(utf_text.encode('utf-8', 'ignore'))
    elif section_type == "0x4":   # SECTION_DOUBLES
        print("DOUBLES:")
        for cnt in range(0, section_length, 8):
            doubles = struct.unpack("<d", data[offset + cnt:offset + cnt + 8])[0]
            print(doubles)
    elif section_type == "0x5":   # SECTION_WORDS
        print("WORDS:")
        words = struct.unpack("<%dL" % (section_length / 4), data[offset:offset + section_length])
        print(words)
    elif section_type == "0x6":   # SECTION_COORD
        print("COORDS:")
        coord1 = struct.unpack("<d", data[offset:offset+8])[0]
        coord2 = struct.unpack("<d", data[offset + 8: offset + 16])[0]
        print("(" + str(coord1) + "," + str(coord2) + ")")
    elif section_type == "0x7":   # SECTION_REFERENCE
        print("REFERENCE:")
        reference = struct.unpack("<L", data[offset: offset + section_length])[0]
        print(reference)
    elif section_type == "0x9":  # SECTION_ASCII
        print("ASCII:")
        ascii_text = struct.unpack("<%ds" % section_length, data[offset:offset + section_length])[0]
        print(ascii_text.encode('ascii', 'ignore'))

    offset += section_length
    print("")

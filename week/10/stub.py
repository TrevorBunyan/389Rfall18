#!/usr/bin/env python2
# from the git repo
import md5py
import re
import socket

#####################################
### STEP 1: Calculate forged hash ###
#####################################

# Connecting to the notary
host = '142.93.118.186'
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Receiving signature from the notary
print(s.recv(1024))
s.send('1\n')

print(s.recv(1024))
message = 'RIP?'          # original message here
s.send(message + '\n')

data = s.recv(2048)
print(data)
legit = data[data.find('hash: ') + 6:data.find('hash: ') + 38]      # a legit hash of secret + message goes here, obtained from signing a message

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'Got You!'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
message_length = len(message)
secret_length = 6           # lowest length of the secret
malicious_length = 8
message_size = ['\x50', '\x58', '\x60', '\x68', '\x70', '\x78', '\x80', '\x88', '\x90', '\x98']
current_size = 0

while(data.find("CMSC") == -1):
    s.send('2\n')

    padding = '\x80'
    for x in range(55 - message_length - secret_length):
        padding += '\x00'
    padding += message_size[current_size] + '\x00\x00\x00\x00\x00\x00\x00'

    payload = message + padding + malicious

    s.send(fake_hash + "\n")
    print(s.recv(1024))
    s.send(payload + "\n")
    data = s.recv(2048)
    print(data)

    secret_length += 1
    current_size += 1

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

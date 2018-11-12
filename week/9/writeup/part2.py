#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331    # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

valid_hashes = hashlib.algorithms_available

for i in range(0,10):
    data = s.recv(1024)
    print(data)
    words = str(data).split(' ')

    hash = words[len(words) - 2].split('\n')[0]     # Value to be hashed isn't separated by a space, it has a '\n'
    hash_type = None                                # If no hashtype is found an error should be thrown
    for word in words:
        if word in valid_hashes:
            hash_type = word

    h = hashlib.new(hash_type)
    h.update(hash)
    result = h.hexdigest()
    print(result)
    s.send(result + '\n')

data = s.recv(1024)
print(data)

# close the connection
s.close()

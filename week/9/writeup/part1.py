#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashes = open("../hashes", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
    for word in wordlist:
        hashed_password = hashlib.sha512((salt + word[0:len(word) - 1]).encode('utf-8')).hexdigest()
        for hash in hashes:
            if hashed_password == hash[0: len(hash) - 1]:                           # Removes '\n' from hash in file
                print("Original Password: " + word + "Salt: " + salt)

        hashes = open("../hashes", 'r')

    wordlist = open("../probable-v2-top1575.txt", 'r')
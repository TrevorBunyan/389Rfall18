Writeup 7 - Forensics I
======

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 7 writeup

### Part 1 (40 pts)

1. It is a JPEG file. I found this by opening the file with Preview and then using the show inspector window. I found all of the information for the other questions using the same technique, except for the flag.

2. The photo was taken from the John Hancock Center (875 North Michigan Ave) in Chicago, Illinois.

3. The photo was taken on August 22nd, 2018 at 16:33:24 UTC. 

4. An iPhone 8 back camera 3.99mm f/1.8 took the photo.

5. The answer was taken at an altitude of 539.54 meters above sea level.

6. I found the flag CMSC389R-{look_I_f0und_a_str1ng}, I found this by opening the file in a text editor and using command-f to look for CMSC.

### Part 2 (55 pts)

Before I started reverse engineering the binary I thought I should first use other methods to analyze it. I used the strings command to check if there were any obvious flags in the binary, but the only useful information I found was a string saying "Where's the flag?" followed by many random symbols. I deduced that the flag was related to the symbols that followed and that I would need to somehow decode it. Then I tried running the binary, which printed "Where's the flag". 

After this I began disassembling the binary. My reasoning was that having an understanding of what the program did would likely lead me to the flag. I used Radare2 to do the disassembly and then I examined the main function. I saw that the program printed "Where's the flag?" to stdout, called a function named reverse_array, and wrote to a file. Based on the previous instructions and the comments in the instructions, I figured out that the file was located in the /tmp directory and was named ".stego". 

Using the file command I saw that it was of type data, so I used xxd to examine the file. I noticed that the magic bytes for the file contained only "JFIF" and '.'s, leading me to check if it was a jpeg file. I copied the file using the cp command to a new file with the .jpg extension. I installed hexedit so that I could modify the file, then I changed the magic bytes to match the jpeg format. This revealed that the file was actually a picture of a stegosaurus, so I knew that steganography was going to be needed to find the flag. I installed steghide in order to find any information that may be hidden in the file. My initial idea was to crack the password by brute forcing it, but before I began trying I thought that I should try using the object in the picture, "stegosaurus". Using steghide to extract with the flags -p to specify the password, "stegosaurus", and -sf to specify the file created a new file named "flag". After using cat on it I found the flag CMSC389R-{dropping_files_is_fun}.

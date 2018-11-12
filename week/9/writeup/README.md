Writeup 9 - Crypto I
=====

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 9 Writeup

### Part 1 (60 Pts)
When I began writing this script I knew the general idea behind the hashcracking was simple, especially since I was asked to create a brute force algorithm. I started by creating a nested for loop structure to iterate over every possible salt and password combination, and to compare it against the hashes in the file. I also realized that I needed to reopen the file after I exited each for loop in order to start from the beginning again. The largest bug I ran into was accidentally leaving the newline character retrieved from iterating over the files. Once I removed it, my script worked normally and generated the following output.
![Part 1 Output](https://github.com/TrevorBunyan/389Rfall18/blob/master/week/9/writeup/images/part1.png)


### Part 2 (40 Pts)
Initially when I was constructing this script, I thought that the questions were the same every time a connection was established. However when I ran this version of the script I quickly realized that the questions changed every time. Thus I decided to parse the response I got from the server in order to find the hash algorithm desired and the characters provided as input to the algorithm. Finding the input was easy since it was the very end of the response, but to find the desired hashing algorithm I split the string at every space, then iterated through the resulting list until a valid algorithm type was found.

After finding those two pieces of information the rest of the script was simple. I used hashlib to get the hash, then sent it to the server. I used a for loop to do this 10 times (the total number of questions) and printed the information I found and received at every step. When I ran the script I got the following output.
![Part 2 Output](https://github.com/TrevorBunyan/389Rfall18/blob/master/week/9/writeup/images/part2.png)


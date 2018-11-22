Writeup 10 - Crypto II
=====

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 10 Writeup

### Part 1 (70 Pts)
When I began creating this script I initially designed it so that I could manually test the forged signature. However after trying several times, I realized that having the script handle connecting and sending input to the server would be much easier. It would also handle changing hashes and varying secret lengths. I knew that as long as I used the same message the hash would not change, but every time I connected a new secret would be generated. Based on this reasoning I decided to use a socket to connect to the server.

The first task I had to complete was parsing the hash from the notary's response. I found the substring that contained "hash: " and then took the next 32 characters (as there is always 32 characters in this hash) as the legitimate hash.

Then I had to create the padding for each attempt at forging the signature. Knowing that the secret was between 6 and 15 bytes allowed me to test each secret + message length, so I added an appropriate amount of '\x00' based on the length of it. Lastly I had to add the correct secret + message length to the end of the padding. I used an array containing the hex values for the possible secret + message lengths and iterated through it, appending it to the end of my padding.

My script continues to try different secret lengths until it sees a flag in the server's response. It prints the result to the console, which gave me the flag CMSC389R-{i_still_put_the_M_between_the_DV}.
![Part 1 Output](https://github.com/TrevorBunyan/389Rfall18/blob/master/week/10/writeup/images/flag.png)

### Part 2 (30 Pts)
To generate a key you can use the command "gpg --generate-key" which will prompt the user to provide a user-id and email. Importing a public key can be done through the "gpg --import <filename>" command. Finally, encrypting a message for someone else can be done with the command "gpg -e -r <recipient id> <file to encrypt>". The -u flag can used to sign it, proving that you are the sender. 


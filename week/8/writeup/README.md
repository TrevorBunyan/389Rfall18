Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. They used the traceroute command on csec-vip.umiacs.umd.edu, which I found by filtering for UDP packets and then checking the destination ip on shodan.io.

2. The hackers go by "laz0rh4x" and "c0uchpot4doz". I found this in some TCP packets.

3. The hackers IP addresses are 104.248.224.85, which is in Wilmington, Delaware, and 206.189.113.189, which is located in New York.

4. They are using port 2749 to communicate on the server.

5. They mentioned that they planned something tomorrow at 1500.

6. One of the hackers sent the other a link to google drive, which contained a file named "update.fpff". The link to the file is https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view. They also said that they gave a parser for the file last week.

7. The hackers expect to see each other tomorrow.

### Part 2 (55 Pts)

1. It was generated on 10/24/2018 at 20:40:07.

2. The author of the file was laz0rh4x.

3. The file says it has 9 sections, however in actuality it has 11 sections.

4. 
ASCII:
Call this number to get your flag: (422) 537 - 7946

WORDS:
(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9)

COORDS:
(38.99161,-77.02754)

REFERENCE:
1

ASCII:
The imfamous security pr0s at CMSC389R will never find this!

ASCII:
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

COORDS:
(38.9910941,-76.9328019)

PNG:
*A png file*

ASCII:
AF(saSAdf1AD)Snz**asd1

ASCII:
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9


DWORDS:
(4, 8, 15, 16, 23, 42)

5. I found the flag "HACKERS" by using a t9 decoder and reading through the possible words that could be created. I also found the flag CMSC389R-{h1dd3n-s3ct10n-1n-f1l3} by using Base64 decoding on the second to last ascii section. The final flag I found was CMSH389R-{PlaIN_dIfF_FLAG}, but I am uncertain that it is the correct flag since there is a missing 'C' in the indicator that it is a flag.

Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 2 writeup

### Part 1 (45 pts)

1. Kruegster1990's real name is Fred Krueger.

2. Fred lives in Silver Spring, MD, based on the information I found on his stwity profile. His email is kruegster@tutanota.com and he is the owner of Cornerstone Airlines according to the company website. He also has reddit and stwity, accounts, which I was able to find by googling the username.

3. The IP address is 142.93.118.186 which I found by using the website ipinfo.info. I also found this IP when I used the whois command in Kali.

4. I found a directory /secret from the robots.txt file. The flags I found were CMSC389R-{h1dden_fl4g_in_s0urce} and CMSC389R-{fly_th3_sk1es_w1th_u5}.

5. The IP address for the admin page is 142.93.117.193. I found this in the URL of the admin page.

6. The servers I found were located in New York, New York. I discovered this by providing the IP address to shodan.

7. The operating system for the server is Ubuntu. I found this by entering the IP into censys.

8. *(BONUS)* The flags I found during this assignment were CMSC389R-{fly_th3_sk1es_w1th_u5}, CMSC389R-{h1dden_fl4g_in_s0urce}, and CMSC389R-{c0rn3rstone-air-27670}.

### Part 2 (55 pts)

I first looked for the correct port number. I used nmap -p1-2000 to find the open port, then connected to it using the nc command to verify it. Then I wrote the brute force script, using a for loop to iterate over all passwords in rockyou.txt. I concluded that "kruegster" was the most likely username since that was his email. After I ran the brute force script to crack the password, I went into the home/flight_records directory. I saw on Krueger's instagram that he was on flight AAC27670, so I used the grep command to look for any flags inside of the file AAC27670.txt. I found the flag CMSC389R-{c0rn3rstone-air-27670} in the file. 

Writeup 3 - OSINT II, OpSec and RE
======

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 3 Writeup

### Part 1 (100 pts)
Firstly, the current login credentials need to be improved. Using a weak password such as "pokemon" makes the server susceptible to brute force attacks. Instead, all passwords should be a combination of numbers, differently capitalized letters, and symbols. This increases the number of potential passwords considerably. Another security improvement is adding a two-step verification system. One option is giving each administrator a physical security key. This addition would make it much more challenging for attackers to access the system since they would need two different complex pieces of information to login, in addition to the correct username.

Secondly, the admin page should not display the IP address of the admin server. Connecting these two servers makes it extremely easy to find the IP address of the administrator server, showing malicious attackers exactly where to go. Removing the admin page is the best solution for this issue. Admins can be given the IP address, rather than giving it to any viewer of the site. By removing this page, it will be considerably harder to locate the admin server and begin an attack.

Finally, the server should set a limit for how many attempts at a login can be made from one connection. The brute force attack was successful since the server had no prevention for repetitive login attempts. Setting a limit for how many attempts can originate from one client would prevent a similar attack from happening in the future. It would also prevent unwanted traffic, since repetitive connection attempts send a large amount of information to the server.
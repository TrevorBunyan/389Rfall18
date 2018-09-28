Writeup 3 - Pentesting I
======

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 4 Writeup

### Part 1 (45 pts)
I was able to exploit the uptime monitoring system by using a command injection attack. After connecting to port 45 of cornerstoneairlines.co, I was prompted to provide an IP address to see if it was up. Since this input was used for the Linux ping command, I could add additional commands to the IP address that would be executed as well. It also meant that I would have all the privileges that this application has, therefore I would have access to many common linux commands. Researching online on OWASP (Open Web Application Security Project) taught me that many linux commands can be exploited by adding certain special characters to the input. I inputted "143.93.117.193; ls", since that was an IP address that Fred has used for his admin server in the past, the semicolon can be used to provide additional commands without having the first be successful, and the ls command would print out the contents of the current directory.

The attack was successful, providing me the output from the ping command followed by the contents of the root directory. This lead me to trying an input without a valid ip address, such as ";cd home && ls", which provided my with the contents of the /home directory without any of the output from the ping command. This command also revealed the file flag.txt, which contained the flag CMSC389R-{p1ng_as_a_$erv1c3}. I used the cat command to find this flag, after first trying the more command.

To protect from this vulnerability, Fred should check that the provided input is valid before executing any commands. Ensuring that the input is in the correct format of an IP address would prevent any inputs containing additional commands from being executed. A regular expression would be able to accomplish this rather easily.

### Part 2 (55 pts)
Once I found the vulnerability I knew that I had access to many Linux commands, but I was only able to issue one set of commands at a time. This meant that I would have to reconnect every time I wanted to provide new commands and my working directory would not be saved. Thus, when I began making the shell I knew I would have to keep track of the directory locally and that I would have to make repetitive connections.

Normally when you connect to port 45, a welcome message is displayed and it prompts the user to supply input. I discarded this output as soon as I received it, instead showing the user the current working directory, mimicking a real shell. I was also able to remove the normal output from the monitoring service by only issuing a colon and the users desired commands.

I created my shell so that it would take a command from the user, then add a command to the start of it to change into the appropriate directory. Also, when the user only changed the current working directory I did not have to connect to the server, since it was stored locally.

I was able to download any ASCII text file by using the cat command to see the contents of a file, then saved it to a new file using the path provided by the user. A user could use the command "pull <remote-path> <local-path>" to download the file, where the local path is beginning from the current working directory on the users system. 
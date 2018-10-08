Writeup 5 - Binaries I
======

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 5 Writeup

When I first began contemplating the problem, I realized that the two functions were very similar. The only difference between the two of them was that the memset function sets the first n characters of a string to one value, whereas the strncpy function sets the first n characters of a string equal to another the first n of another string. Based on this information I knew that if I could figure out the basic implementation of one, than creating the other was simple. Thus I wrote the memset function first due to the ease of converting it into the strncpy function.

The next thing I considered was how I would implement these functions in a high-level language. Since an example was provided in C, I was able to understand the basic components my function should have. I realized that a simplistic approach was to create a loop that iterated through the string, setting the character at each index to its appropriate value. However, my implementation in assembly differed from the provided example due to my use of the loop instruction. Instead of counting from 0 to strl or len, I set the rcx register to strl or len, then used the loop instruction to decrement it after each iteration.

After I created my loop structure I encountered an error with the amount of bytes I was using in the mov instruction. I was using the full 64 bits when I should have only used the first eight since a char is a single byte in C. I changed my instruction so that it only copied the first eight bits from rsi and wrote to the first eight bits of memory that rdi pointed to. I also used the inc instruction to increment my register that pointed to memory. This step finished the function, giving me the correct output when I tested it.

Finally, I implemented the strncpy function by examining the difference between it and memset. I noticed that all I had to do was keep a second pointer to a string in memory and increment it after each iteration. I added this functionality, then encountered an error telling me that I was improperly using the mov command. I fixed this by not accessing memory for both the src and dst pointers in the same command, so I used another register to temporarily hold the value from the src pointer.
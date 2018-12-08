Writeup 10 - Crypto II
=====

Name: Trevor Bunyan
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Trevor Bunyan

## Assignment 10 Writeup

### Part 1 (70 Pts)

After investigating the website, I realized that the item page used a parameter called "id" in the URL to determine which item's information to display. The three items displayed on the home page corresponded to ids of 0, 1, and 2, so I decided to try using a different value to see what would happen. The server defaulted to the item that corresponded to id=0, so I knew that it saw the new id as invalid.

Based on hints given on the prompt, I then tried using SQL injection. At first I passed `' OR '1'='1` as the id parameter, but I was given an error back from the server. However, when I tried using some other variations, such as `' OR '2'='3'` I was given the default item again, so I determined that some common SQL commands where invalid as input to the parameter. This led me to my final argument, `' OR 'true'='true`, which generated a page containing the information for every item in the table.

One of the items returned was named "FLAG", and its description contained the flag CMSC38R-{y0U-are_the_5ql_n1nja}. The '9' was missing from the standard flag format, but I assuming that it is a spelling error. I also found the flag separately by passing "1337" as the argument to id since most numbers/references used in this class have been jokes.

### Part 2 (30 Pts)

For the first level, all I had to do was put `<script>alert();</script>` into the text box. I did this on my first try, correctly assuming that it would add the input to the HTML without validating it.

In the second level, I noticed that in the first post the user was able to use HTML tags to alter their post, so I tried repeating the same input from before. However it did not work in this case, so instead I used another tag and added an attribute that would cause an alert. My post was `<p onmouseover="alert();">hi</p>` which caused an alert when I hovered over the post.

The third level used a parameter to determine which image to display on the page. Looking at the HTML for the page showed me that it was taking the string without validating it and adding it to an image tag. I realized that I could add an attribute to the tag and then end it early. To inject the script I used `1.jpg' onmouseover="alert();">` as my argument for the parameter, causing it to show the image and trigger an alert when a user hovers over it.

The fourth level uses user input to determine the length of time for a timer. After trying inputs that might break it, such as negative numbers and symbols, I noticed that it added the user input to the HTML without ensuring it was a number. Based on this information, I used `3'); alert('` as input to the timer. This input would correctly create a 3 second timer, but it would also cause an alert.

For the fifth level, I started by reading through the HTML of each page. A comment pointed out that the user provided input was ignored, so I knew the only point to inject a script would be through the URL parameter used on the same page. For some reason, the parameter is used to determine what page the next button would link to even though it was always the same page. I initially tried to add another element, but whatever I put was bound to the href attribute. I researched what could be provided to the href attribute and found that I could add javascript. I used `javascript:alert()` as the argument to the next parameter, which caused an alert to be shown when the user clicked on what should have been a link to the next page.

The final level used a javascript file loaded from an internal directory, which was provided as a parameter in the URL. To avoid external scripts, "http" was not allowed to appear in the parameter. However this is not case sensitive, so using an uppercase character anywhere in that substring would allow any external javascript file to be loaded instead. I used this oversight to provide a script that caused an alert upon the page being loaded.
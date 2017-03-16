/*
*Michal Chorobik 0937145
*mchorobi@uofguelph.mail.ca
*February 19, 2017
*/

To run the program run the make command.

To add a user to a stream(s):
./add <name of a user>

To post to a stream:
./post <name of the user>

To view the a stream(s):
./view.py <name of the user>

Additional info:
When the name of the stream is given. The program will read the spaces as part of the name when there is more than one stream listed.
You must past an argument as you run the view,post and addauthor programs.
In my program I use the up and down arrows. Once you run the view program you can go up or down.
If you do up and you reach the message at the top the text will stop scrolling up. Once you reach the message at the top and keep on
clicking the up arrow you will have to click the down arrow the same ammount of times to start scrolling down again.
If the screen is ever blank that means that you read all the messages and in order to see the previously read ones you just need to go up.
This happends when you use the o or the s commands. When you use those command on the terminal the list of streams the user is in prints
multiple times as the result of arrows curses being represented by multiple numbers
To end the program press q. ctrl-d on an empty line ends the post program.

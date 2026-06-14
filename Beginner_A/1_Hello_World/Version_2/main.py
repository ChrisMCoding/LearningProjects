print("Hello World!")
input("Please press Enter to continue...")


"""
Welcome to the same program as before but with a whole extra line.

Before we do anything here, it's really important that you know that
the order you write your code in (top to bottom) is the order that the
code will run in. So here, 'print' will run, and *then* input will run.
This is called the 'order of execution' and is important for defining
something called 'the flow of data' which we will worry about later.

And by 'later' I mean 'much later'.

Okay cool, so we have a new line of code, but what does it do?

The exact same thing as the other one! Almost!
This will write "Hello World!" to a console window and then write 
"Please press enter to continue..." to the same console window and
when the user presses the enter key, it will end the program.

But wait, why is the 'input' function writing something to the console?
So the argument that the input function takes is actually the prompt that
it will display to the user to get their input. The user can then type
whatever they want and then it'll try to save what they typed when they press
enter, and continue with the rest of the program.

Note that it can save data, that's a special tool that will help us in the
next version of this program. At the moment, since we haven't told it
to save the data, it'll just bin it, but it's important that it *tries* to
save the data it gets. This is called "returning a value" and we'll
come back to this when we write our own functions shortly.

"""
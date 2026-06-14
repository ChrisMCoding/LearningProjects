# This bit of code won't be run unless something in the bit of code that
# is getting run asks it to be. That would be called "calling" the "main" function.
def main():
    username = input("Please enter your name: ")

    print(f"Hello, {username}!")

    input("Please press Enter to continue...")


# This bit of code will be run when the program starts
if __name__ == "__main__":
    main()


"""
Okay so we've added something at the bottom of the file but like, why though. Why'd we do that.

First things first, what is it?
That's an 'if' statement. An 'if' statement defines a condition, and says 'if this condition is met,
then run the next bit of code'. In this case, our condition is ' __name__=="__main__" '.
Here, the '__name__' bit is a variable that python uses to record what file the code that is 
running came from and whether it's the file the user clicked or had open to start with, or it's 
being run by another program (called 'importing', we'll deal with that later) and not the user. 
If the user specifically asked this file to run, then python will name it '__main__', and the 
'==' symbol is used to *ask* if two things are the same. But why's it got those two underscores
on either side? These are called 'dunder' variables, short for double underscore, and python
uses them to keep track of its own data.

In other words, that bottom bit says:
        If the variable called '__name__' has the value "__main__", then do the thing in the next bit of indented code.
                Or in useful terms
        If this file is the file the user manually ran themselves, then do the next bit of indented code.
And the next bit of indented code says:
        Run the function called 'main'.

It's important to note that any code that is part of a function definition (the indented bit after 'def main():')
won't run unless you specifically ask it to somewhere else in the codebase, as in the bit at the bottom of the file.

This pattern (having a main function and a bit that says 'if __name__=="__main__":' and putting your whole
file in a 'def main():' function) is called a 'main guard' and it prevents code from running
unless the user specifically asks the code to run, or the file the user wanted to run wants this other bit
of code to run. It is useful for later, right now it should appear *utterly useless*.
"""
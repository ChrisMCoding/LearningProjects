# This bit of code won't be run unless something in the bit of code that
# is getting run asks it to be. That would be called "calling" the "main" function.
def main():
    username = input("Please enter your name: ")

    print(f"Hello, {username}!")

    input("Please press Enter to continue...")


# This bit of code will be run when the program starts
main()


"""
If you're looking at the code below and thinking:
        What
Don't worry, but this will be a little more complicated to explain, and this is
mostly just setting up for Version 5, which we'll get to shortly and it'll be
pretty confusing for a little while, but bear with! At the moment we're just
setting up what's called an 'entry point' to the program. When the program
gets larger this will make it easier to follow what's happening.

So what's going on in the code?
Well let's start with this: What's a 'def'?
'def' is short for 'define' and this is what's called a 'keyword'.
A 'keyword' is just a word that python uses for a specific purpose, and more importantly,
that you can't use for anything else. Don't worry, they're colour coded so you'll
know if you write one.
The 'def' keyword is used to say "the next thing I write is the name of a function
and I'm going to write out what the function does". In other words, the 'def'
keyword lets you define a function, and a function is just a bit of code that
does something.
In our case, the function we're writing is called "main" and that means, just like
with a variable, if we want to run this function, we just write "main()" and the function
will run.

Next question, why do we have empty brackets after 'main' and why do I have to write
those when I want to use the function?
Those mark out where the arguments for main would go, and if there aren't any arguments
they just tell the computer that the thing just before them is a function, not a variable.
They basically say "this thing I just wrote references another bit of code, please go to
that bit of code and do what it says, then come back here".

What's the colon for and why is the next line indented by 1 tab?
The colon tells the computer that the next bit of code is the code to run whenever
it sees 'main()' written anywhere, in other words, that is the definition of the function.
That's the code to run for that function.
The indentation, however, tells python where the code that the function will run starts and ends.
Typically in python, people use 4 spaces for indentation, but I like to use tabs, the only important
thing is that it's the same everywhere because whichever you start using, python will expect everywhere
and if it sees something else it will get confused and break.
But basically after a colon, the code that's going to run needs to be indented to tell python that it belongs
to the thing that came before it. When you then go back to writing without the indent,
that tells python that the code you're writing does *not* belong to anything and can be run
or read as normal. This will get more complicated, you'll figure it out, I promise, but for now
just know that this is part of something called 'defining scope', and a scope is just the area
in which specific bits of data can be accessed.

Finally, that last bit at the bottom is just running the function we wrote. Because that function
is defined in the 'def main():' bit, it doesn't actually get run unless we call it somewhere,
and we do that exactly the same way we called 'print' and 'input' before, but right now, 'main'
doesn't take any arguments, so we just leave the brackets empty to say "this is a function, it 
doesn't need any data to run, just go do it".
"""
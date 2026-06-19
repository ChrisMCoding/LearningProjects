import random as rand

randomNumber = rand.randrange(1, 10, 1)

userGuess = int(input("I'm thinking of a number between 1 and 10, take a guess at what it is: "))

while(userGuess != randomNumber):
    userGuess = int(input("Not quite! Try again: "))

input("You got it! Press any key to close the program...")


"""
In this example we have a lot here that's quite new if not completely new. From the top!

The 'import' keyword! What's that?
So the 'import' keyword says "go to this other place and get a bit of code from it so that
I can use it here". It's coupled with the 'as' keyword here which allows us to name the thing
we import differently so it's easier to use. So that first line, in regular English says:
        Import the bit of code called 'random' and call it 'rand' in this file.

Next one, let's go, why does 'int' have brackets, what's going on there? Also what is 'int'?
So 'int' is short for 'integer' and it's what's called a data type. For more detail on that
take a look at 1_Hello_World/Version_3, there's a footnote there on data types which explains
more about how they work. But the brackets, why the brackets? That's called 'casting' and that's
where we say 'take this value and try to turn it into this other data type'. So 'casting' is
our way of telling the computer to try to treat some data as a different kind of data than it
reports to be. In this case, take a string, and try to read it as an integer.

That allows us to take some text as input from the keyboard and read it as an integer, which means
we can start adding it to things, subtracting it from things, or asking if it's the same as some
other number.

Now we have a whole new logical concept! Loops! One of the fundamental pillars of programming!

LOOPS!

Thrilling! What are they?
Loops are areas of code which we ask to repeat, to run again a set number of times or until
some condition is met. In this case, we have a 'while' loop which is a kind of conditional
loop. What we're doing here is we're asking the indented bit of code to run until the user
guesses the right number, using... '!='? What? What's that? So normally if we're asking
a question like "is a equal to b" we use two equals symbols, so we would write that as
"a == b", but if we want to ask if a is not the same as b, we use an exclamation mark
instead of the first equals sign. We write that as "!=", so then the 'while' line is, in
plain English:
        While userGuess is not the same as randomNumber, do this indented bit of code.
And that's while loops! There are other kinds of looks, but the most common are 'for' loops
and 'while' loops, typically you want to use 'for' loops if possible, but that's not always
possible. This is one of those cases where it is not possible, or practical, to use a 'for'
loop. But what's a 'for' loop? Good question, we can deal with that later but for now, just 
know that we need to know how many times we want to run the indented bit of code before
the loop to use a 'for' loop.

Wonderful, now we have while loops covered, we can write much more complex programs!
"""
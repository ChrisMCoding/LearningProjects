def greet(name: str):
    """Write "Hello" and the user's name in the console."""
    print(f"Hello, {name}!")

def wait_for_user_input():
    """Pause the program until the user presses enter."""
    input("Please press Enter to continue...")

def main():
    username = input("Please enter your name: ")
    greet(username)
    wait_for_user_input()

# This bit of code will be run when the program starts
if __name__ == "__main__":
    main()


"""
This looks confusing but first thing's first, is this actually any different from the last version?
Short answer: no.
Long answer: no, but this is written in a way that is easier to read (it's not right now
but hopefully it will be in a second) and, more importantly, it's easier to add more stuff 
to it later.

So, first things first, what's a 'str' and why's it in my code?
In version 3 we added the ability for the user to enter their name and let the computer
greet them, by name. In that version there was also a footnote on data types, so you
can refer to that for more details, but tl;dr, 'str' is short for 'string' and a 'string'
is just text. We use these to tell the computer how to store and read the data we give it.

So now we know a bit about the types, what's going on with that greet function?
Why's it got a 'name' in brackets and what's with the ': str' after it?
Cast your mind's eye back to version 1, where we talked about arguments, and giving functions data.
Here, because we are writing the function, if the function needs any data, we also need to say what
kind of data it needs, and what to call all the bits of data so that we can reference them later.
In this case, the 'greet' function needs some text that we're calling 'name' because we're going to
use it as if it were someone's name. So since we're defining a function here, in the brackets 
where you'd normally put the data you're sending to the function, you instead put the name of the
data you expect to be sent to the function, and then a colon and the type of data you expect after
that.

Also, what's going on with passing 'username' to the 'greet' function and then using a different
variable called 'name' in the function itself (otherwise known as the 'function body')?
Well when we pass a variable to a function, we're actually just telling the computer to use the
data that the variable refers to. When we do that and go to the function, it just has the data,
it doesn't know exactly what to do with it, so we have to tell it to name it something so 
we can access it in the function body. It's helpful to think about variables as a bunch of data
kept somewhere, and a separate name that we use to tell the computer to go find that bunch of data.

Okay, last thing, what are those triple quotation mark bits at the start of each function?
In version 1 we were introduced to doc-strings, and these are those! The best way to demonstrate
what they do, is to simply hover your mouse over where the functions are called, and in the 
helper text that pops up you should see the doc-string text for that function! This helps us to
use functions properly and to remember what functions do, and actually, they help us to see
when our functions are doing too much stuff and are liable to get *very complicated* which is,
usually, a very bad thing for us if we want to add more stuff.
"""
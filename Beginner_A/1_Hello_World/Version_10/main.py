def get_name() -> str:  
    """Request the user's name and return it."""
    name = input("Please enter your name: ")
    name = name.strip()
    return name

def greet(name: str) -> None:
    """Write "Hello" and the user's name in the console."""
    print(f"Hello, {name}!")

def greet_user() -> None:
    """Request the user's name and write a greeting in the console."""
    name = get_name()
    greet(name)

def wait_for_user_input() -> None:
    """Pause the program until the user presses enter."""
    input("Please press Enter to continue...")

def main() -> None:
    greet_user()
    wait_for_user_input()

# This bit of code will be run when the program starts
if __name__ == "__main__":
    main()
    

"""
This looks about the same as the last one, so what's new?

First of all we've renamed 'username' to 'name' in the 'greet_user' function
because it's a bit of a nicer name. So that's good.

Next, if you have a look at the 'get_name' function you'll see a new function
called 'name.strip()'. What's going on here? Isn't 'name' a variable?
Yes, it is a variable, but what's important here is the data type. The
variable 'name' is a string and strings actually own some data and functions.
Functions that are owned by something are actually called 'methods' which,
I mean, ain't that important a distinction? But basically, the important thing
to know about them is that they can access the other data that belongs to
the same thing that the method belongs to. This will take a minute to get used
to, so don't worry too much about it, you'll get used to it, I promise.

Anyways, now that we know that string owns functions, or methods, it's time
to address 'name.strip()'. The method is actually called 'strip' and it belongs
to the string data type. Because this method actually belongs to the string
data type, and more specifically belongs to our variable 'name', we say it is
being called 'on' the variable 'name', which means it will do something to the data that
'name' references. The '.' in between the two indicates ownership, so
'name.strip()' can be thought of as calling 'name's method, called 'strip'.

Ideal, okay, so now we've got that down, what does 'strip' do? What it does is
it takes the data that it was called 'on' and it looks for spaces or tabs
at the start or end of the string and removes them. To help explain this one,
let's imagine we had the value " Amy". Notice that it starts with a space,
if we ran 'strip' on this value, it would remove the space and turn it into
"Amy". Stunning! We've just performed a simple form of 'input validation', which
is when you check or alter data to make sure that it won't cause problems
for the rest of the program.

But wait, why are we writing 'name = ' before the 'strip' method call? Isn't
that used to assign data to a variable name? I thought we were modifying the data
in 'name' anyway in the 'strip' method?

While the '.strip()' function call will use the data held in the 'name' variable,
it won't actually modify the data directly, instead it will return the modified
version, and leave the original data untouched, so if we want to actually modify the original
data, then we have to assign the variable 'name' it's new value, which will be
the value returned by the 'strip' method. To answer the question:
        Why would I ever want it to *not* replace the old data?
The only thing I've got is that there may be specific circumstances under which you
actually want the old data back later on, so python gives you the option to not
overwrite it, just in case. That's really all it is though!
"""
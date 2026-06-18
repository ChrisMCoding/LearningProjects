def sanitise_input(text: str) -> str:
    """Removes any characters in the user's input that we don't think should be in names"""
    sanitisedInput = text.strip()
    return sanitisedInput

def get_name() -> str:  
    """Request the user's name and return it."""
    name = input("Please enter your name: ")
    return name

def greet(name: str) -> None:
    """Write "Hello" and the user's name in the console."""
    print(f"Hello, {name}!")

def greet_user() -> None:
    """Request the user's name and write a greeting in the console."""
    name = get_name()
    name = sanitise_input(name)
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
Okay, I know in the last one we had 'input(...).strip()' and we had just put it in one line
and we didn't have lots of extra variables and assignments like before and in this one we've
got a whole new function called 'sanitise_input' but there's a reason for that! And
incase you're thinking:
        Couldn't you write 'return text.strip()' in the 'sanitise_input' function?
You're absolutely right, we could write that! but we've split it onto two lines for something
called 'debugging' which is the process we use to fix faulty programs. We'll cover
why using two lines here makes that easier later but for now, just know that assigning
values and returning values, and processing values, should all be done on separate lines.

If you remember that whole single responsibility thing from a couple of versions
ago, this is more of that. Technically that 'strip' method was actually a form
of sanitisation which would have meft the input function with two responsibilities.
For a program like this, that doesn't matter, but it is a little better to
have sanitisation in a separate function.

But wait I'm getting ahead of myself, what's sanitisation?
Sanitisation is the process of altering data so that it's either easier to work
with or it follows some rules that we want it to, in this case, we don't want
any spaces at either end of the user's input.

Brilliant, but what if there isn't a way to alter the data so that it's useable?
Well, that's where validation comes in, and validation is just the process of
checking that data adheres to all the rules we've set for it, and rejecting
the data if it doesn't. We'll cover that in the next version though, worry not!
"""
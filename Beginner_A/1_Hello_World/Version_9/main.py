def get_name() -> str:  
    """Request the user's name and return it."""
    name = input("Please enter your name: ")
    return name

def greet(name: str) -> None:
    """Write "Hello" and the user's name in the console."""
    print(f"Hello, {name}!")

def greet_user() -> None:
    """Request the user's name and write a greeting in the console."""
    username = get_name()
    greet(username)

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
This looks pretty similar to the last one but now we have arrows everywhere.
Is it actually different? No, but it is easier to add to.

Let's begin with: What's going on with that weird '->' sign?
That symbol tells us what kind of data the function will 'return', or in normal speak,
what kind of data the function will attempt to store somewhere, or be replaced by, if we run it. 
Think of it as a label on a machine, the function, which tells you what comes out 
when you press start. 
Note, it won't actually store the data unless we assign it a variable, but it will 
make it available to be stored if we are so inclined.

Okay so why do we have '-> None' then?
That tells us that the function does something, but doesn't try to store anything once it's done.
It's how we say "this function isn't going to be replaced with anything when it runs, it will
just do something, and won't say anything after it's done".

Why do we need to do that?
You don't, but it tells the computer whether to expect data after a function is run and what kind
of data to expect. That means that it can tell the programmer (that's you) if they're (read: you're) 
about to make a grievous error.

For example, if I wrote:
        def func() -> str:
                return 5
Then the computer would complain bitterly and tell me that 5 is not text, and I
promised it text, so I need to fix that.

That'll stop us (in theory) from making silly mistakes later down the line, so it's just good
practice to write like this. It won't actually make a difference for our functionality, but it 
will help us to write more complicated things without getting tangled up or making mistakes.
"""
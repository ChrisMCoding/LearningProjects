def get_name():  
    """Request the user's name and return it."""
    name = input("Please enter your name: ")
    return name

def greet(name: str):
    """Write "Hello" and the user's name in the console."""
    print(f"Hello, {name}!")

def wait_for_user_input():
    """Pause the program until the user presses enter."""
    input("Please press Enter to continue...")

def main():
    username = get_name()
    greet(username)
    wait_for_user_input()

# This bit of code will be run when the program starts
if __name__ == "__main__":
    main()


"""
We have *more* functions now and we've got a new keyword called 'return' now, that's great,
however, we gotta figure out what's going on with all this new stuff.

What's the deal with that 'return' keyword?
The 'return' keyword is used to tell the computer that the next bit of data is the data that the
function is going to send back to wherever it was called from. In other words, this is the data
that the function will try to store when it's done. In fact, it's actually pretty useful here
to think of each function call being replaced with the data it 'return's, because when the code
runs, that's basically what's going to happen.

We still got a couple of questions here though, like, why the hell is 'get_name' a function, it looks
identical to the 'input' function. Why'd we go do that? Same with the 'wait_for_user_input' function!
Why have we done this!? It's pointless! Surely!?

Well, yes, for now. What we're doing here though, is we're putting the bit of the code that deals
with waiting and the bit that deals with user input somewhere away from all the other code. 
What that means is if we want to change how they work, like how we're getting user input, 
we can do that without editing any other parts of the code. This will be incredibly useful when
we get to more complex functionality, just, like, trust me, bud.
"""
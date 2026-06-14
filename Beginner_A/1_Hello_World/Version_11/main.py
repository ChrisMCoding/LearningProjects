def get_name() -> str:  
    """Request the user's name and return it."""
    name = input("Please enter your name: ").strip()
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
This one's not that different again, what gives?

If you have a look at the 'get_name' function you'll see '.strip()' written
after the 'input' function call. Wasn't that just on the next line? Wait,
didn't we want to call that on 'name'?

Yes! More specifically we wanted to call it on the user's input. Now,
here we gotta remember what I mentioned earlier about functions being more
or less replaced by the data they send back or try to save. There's actually
a little more to it than that, see, it's not just that functions get replaced
by a value, the function call itself is treated by python as if it is the
data it returns! So python is treating 'input()' as a string, and letting
us call methods that belong to the string data type, which is exactly what
we're doing here. In other words, this is quite literally exactly the same
as the previous version, we've just moved our function call to make it a bit
shorter, without making it significantly harder to read.
"""
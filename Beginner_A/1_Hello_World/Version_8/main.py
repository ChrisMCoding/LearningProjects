def get_name():  
    """Request the user's name and return it."""
    name = input("Please enter your name: ")
    return name

def greet(name: str):
    """Write "Hello" and the user's name in the console."""
    print(f"Hello, {name}!")

def greet_user():
    """Request the user's name and write a greeting in the console."""
    username = get_name()
    greet(username)

def wait_for_user_input():
    """Pause the program until the user presses enter."""
    input("Please press Enter to continue...")

def main():
    greet_user()
    wait_for_user_input()

# This bit of code will be run when the program starts
if __name__ == "__main__":
    main()


"""
So there's one new function here called 'greet_user' and all it does is call other functions, 
neat-o, but why?

Well if you have a look at each function here, you'll notice that some of them are only doing one thing
and some of them are combining those functions that only do one thing. 
The 'get_name' function gets the user's name from input and that's it. The 'greet' function
writes the user's name to the console and that's it. The 'greet_user' function combines these two
functions into one function that does two things by using other functions, but itself doesn't do anything
except call other functions. The 'wait_for_user_input' function just waits for the user to press enter.

And finally the 'main' function combines our 'greet_user' and 'wait_for_user_input' functions.
This means that all of our logic is squirrelled away in functions that only handle one thing each,
and it's all combined in orchestrator functions that just call those functions and don't do anything themselves.
This means that if we want to add new functionality or change how something operates, we only need to
look in one place and we can just worry about what our new thing is doing, without worrying about how it
interacts with anything else. This makes writing code for larger projects easier, and it's called the
"Single Responsibility Principle"; each function should only do one thing.
This also means our code is reusable, and thanks to the descriptive names we used, it's actually
easier at a glance to see what our 'main' function is doing. It's greeting the user, and then it's waiting
for input before it ends.
"""
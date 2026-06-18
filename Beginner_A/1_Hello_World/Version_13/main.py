def sanitise_input(text: str) -> str:
    """Removes any characters in the user's input that we don't think should be in names"""
    sanitisedInput = text.strip()
    return sanitisedInput

def is_input_valid(text: str) -> bool:
    """Checks that the user's input follows the rules we decided for names"""
    isValid = True
    if len(text) <= 2:
        isValid = False
    return isValid

def validate_input(text: str) -> str:
    """Runs input validation and returns a default value if validation fails"""
    if not is_input_valid(text):
        text = "Friend"
    return text

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
    name = validate_input(name)
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
Alright, two new functions here, what's happening and why?

We have the new 'is_input_valid' function first, so what does that do?
It applies our rules for validation, basically, it just checks if we are actually
able to use our input or if it breaks rules and we can't make it adhere to them
through sanitisation. A key thing to note here is that we named it as a question,
that's basically just because it makes it clearer what we're doing when we use this
function in an if statement.

Next, why've we got a 'validate_input' function and what's the 'not' thing?
This function basically just acts as an orchestrator function; it runs our validation
and it decides what to do if validation fails. Its responsibility then, is to just
run all of our validation and subsequently decide what to do with the result. 

Next, the keyword 'not', what does it do?
This one's very much what it says on the tin, this keyword just asks "is the answer to the 
next question 'no' and if it is, do the next thing." Let's look at an example condition:
    if 2 == 2:
This condition will 'return true' that is, it'll pass, the next bit of code will run. What
about this one:
    if not 2 == 2:
This condition will 'return false' or fail, because 2 does equal 2, and we're asking if
2 does *not* equal 2, but because it does, our condition is not met, and we will not do
the next thing.

Excellent, now, I do want to stop for a second and acknowledge something:
we have long passed the point of over-engineering here.

If all you need a piece of software to do is greet the user, this became overkill
around version 7. That said, if you needed a piece of software to greet the user
in a production environment, you'd rather have the overengineered one because
that's easier to deal with if one day it needs to do something else.
"""
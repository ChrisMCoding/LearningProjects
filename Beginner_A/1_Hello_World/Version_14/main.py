class DataSanitiser:
    """Alters input to ensure it does not contain anything that could cause the program to fail."""

    def sanitise_input(self, text: str) -> str:
        """Removes any characters in the user's input that we don't think should be in names."""
        sanitisedInput = text.strip()
        return sanitisedInput

class InputValidator:
    """Handles rules for validating input and the execution of input validaion."""

    def is_input_valid(self, text: str) -> bool:
        """Checks that the user's input follows the rules we decided for names."""
        isValid = True
        if len(text) <= 2:
            isValid = False
        return isValid

    def validate_input(self, text: str) -> str:
        """Runs input validation and returns a default value if validation fails."""
        if not self.is_input_valid(text):
            text = "Friend"
        return text

class InputManager:
    """Handles getting user input."""

    def get_name(self) -> str:  
        """Request the user's name and return it."""
        name = input("Please enter your name: ")
        return name

class ConsoleHelpers:
    """Contains useful methods for working in the console."""

    def wait_for_user_input(self) -> None:
        """Pause the program until the user presses enter."""
        input("Please press Enter to continue...")

class DisplayManager:
    """Handles displaying data to the user."""

    def greet(self, name: str) -> None:
        """Write "Hello" and the user's name in the console."""
        print(f"Hello, {name}!")

class Greeter:
    """Manages all functions involved in greeting the user."""

    def greet_user(self) -> None:
        """Request the user's name and write a greeting in the console."""
        inputManager = InputManager()
        inputValidator = InputValidator()
        dataSanitiser = DataSanitiser()
        displayManager = DisplayManager()

        name = inputManager.get_name()
        name = dataSanitiser.sanitise_input(name)
        name = inputValidator.validate_input(name)
        displayManager.greet(name)

def main() -> None:
    consoleHelpers = ConsoleHelpers()
    greeter = Greeter()

    greeter.greet_user()
    consoleHelpers.wait_for_user_input()

# This bit of code will be run when the program starts
if __name__ == "__main__":
    main()
    

"""
Okay we've added a massive amount of code here, but fear not, it's all actually pretty similar.

So you'll see the keyword 'class' everywhere in this file. It might look like each of the
words after are also keywords, but they're not, they are names of classes which we have created.
But what's a class? I'm getting ahead of myself here.

It might be useful here to think of classes as rubber stamps or templates, because in very
loose terms that is what they are. Conceptually, classes act as loose descriptions of things,
abstract or real, but to help explain, let's look at a real life example:
        A book has a cover, pages which contain text, and a blurb. We can say that about *all*
        books (I think) so if we want to model a book in code then we can create a book class.
        This book class will have some data about a cover, some way to store data about pages,
        and a blurb. We should also have some way to move to a different page. Excellent.
It's important to note that the book class doesn't necessarily contain data, it just describes
what data should be there. But, if, for example, all book covers were red, then we could just
store the cover colour as red as a default value. We can do that, but we don't have to, the
class is just a description of books in general.

Okay, wonderful, but what if I want a description of one specific book? In that case I need to
do something called 'instantiation' where I create an 'instance' of a class. In other words, I
tell the computer I want a book, and then it will use the class to create a book for me. I can then
describe the book and this one book that I've created will have the properties I asked for.
It's also worth noting that you can't access the data or methods in classes unless you create
an instance. You need a specific book if you want to look at what's on its pages, for example.

The next question then is: how do I do this 'instantiation'?
So if you want to instantiate a class you need to assign it a variable, to name the instance,
and you need to write the name of the class and then add brackets, just like we did for functions.
That's precisely what we're doing in the 'main' method here; instantiating classes, and then calling
methods on those classes!

With all that said, it might not be obvious how classes are used in modern software development.
Classes are primarily used to encapsulate data and behaviour or functionality; to keep things
organised and to isolate functionality so that it can be swapped if we want to do something
different later. (We won't see classes and behaviours used for swapping right now though.) Rather
than describing some physical or abstract object, they're used to just put related things together
in one place, which is largely what we're doing here. If that doesn't seem useful at the moment,
don't worry, it won't for uh... I'm willing to say quite a while. And if it *does* make sense,
wonderful! The rest of using classes and all the other stuff we pile on top will be fine!

You'll also notice that all these methods now have 'self' as an argument, what is that?
We just talked about instantiation there and specific books being made from our template, or
'class', for books in general. These specific instances have their own instance specific data,
so our instances of books will have, for example, all the data in their pages. When we
pass 'self' into every method, what we're doing is we're letting each method access their
instance specific data, like the data in these pages. So it's just saying "this method can
access the data that its instance has". That might make more sense as we go on so if it doesn't
right now, just pay attention to how classes and instances are used and it will (hopefully) clear up!
"""
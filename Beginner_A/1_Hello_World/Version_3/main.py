username = input("Please enter your name: ")

print(f"Hello, {username}!")

input("Please press Enter to continue...")


"""
This is undeniably a lot more complicated so bear with me as we do our damnest to
completely ignore all the complicated bits.

First of all, what does this do?
This will ask the user (you) to type in your name, and then it will save it to a VARIABLE
and then display the text "Hello " and then the name the user entered, and then an
exclamation mark, and you know the rest.

So what's a variable?
Good question, I'm glad I asked.
A variable is just a value that can change while the program is running, it can vary,
thus the name.
Our variables have names which we use to access them. So our variable which will store
the user's name, is called 'username' and when we want to access the data that we
saved to it, we just type 'username' and the computer will go get it for us.

Wonderful.

Next question, what's that 'f' doing before the quotation marks, and what about those weird
curly brackets (or braces as we call them in 'the biz')?
That's what's called an 'f-string' because you put an 'f' at the front, and basically
it says that the text in the quotation marks will contain references to variables,
and that you want the computer to replace the variable name in the text with the value
that it references. The braces are there to tell the computer what part of the text
is a variable and what part is just regular old text.

Oh that's another thing, use descriptive names! Don't worry about how long they are and use pretty much
any convention you like as long as you don't start variable names with numbers or use spaces. If you have
a really long variable name you can type the first bit of it then press 'tab' and your computer will write the
rest for you. You're better having long unwieldy but descriptive names than short ones that are easy to type
like 'a' or 'x' because at least that way you can tell what a variable is for when you come back to your code
later.
"""





"""
Notes for particularly enthusiastic learners:
DATA-TYPES! What are they and more importantly, why are they?
So a data-type is pretty much what it says on the tin, it's a type of data.
There are a few types of data but the important ones are as follows:

string
A string is just text, anything in quotation marks.

int
An int is just a number that doesn't have anything after the decimal point.

float
A float is a number that *does* have something after the decimal point.

boolean ('bool' for short)
A boolean value is just something that is either a 0 or a 1. We call 0 false, and
1 true, in other words, a boolean value is either true or false.

There are more data types but you might not ever see them and they're a lot
less common than those ones.

But why have data types at all?
Well, the computer just stores a buncha 0's and 1's for all this code and all the
data you use. It doesn't know what any of it means, so you have to tell it how
many 0's and 1's it needs to look at and what they represent for any given piece of
data. That's all that a data type is. It says "look at the next 8 0's or 1's, and
once you've got them all, that represents this thing, so treat it like that".
Without them, the computer doesn't know how to read anything.

That said, python is what's called a 'dynamically typed' language, which means you
don't need to tell the computer what data type anything is, python will figure it
out for you. In other words, now that you know this stuff, feel free to ignore it.

BUT HAVING SAID THAT, telling python what data types you're using will make
your life easier, because if you accidentally send the wrong kind of data somewhere
and you've told python what data-types need to go where, then python will stop
you from sending that data to the wrong place. Python might be 'dynamically typed'
but it's also 'strongly typed' which means if you do give something the wrong
kind of data it'll panic and stop. This can get very annoying because, and trust me
here, you will try to pass the wrong kind of data to the wrong place.
"""
# Practical Python

This is a hands-on workshop which aims to teach practical Python programming skills. The workshop
does *not* intend to be a comprehensive guide or a Python reference. Rather, it aims to provide
people who have little to no Python experience the essentials for making useful things with Python,
with references to more elaborate material on specific topics from time to time.

By the end of this workshop you will have written two real-world projects in Python:

1. An AWS Lambda function which uses the AWS Python SDK ([boto][1])
1. A command-line utility

TODO - explain what the projects do.

To give you the understanding and skills required for writing real-world projects, we will go
through the following topics:

- What is Python?
- 2 or 3?
- Setting up Your Work Environment
- Using the Python Interpreter
- Whitespace!
- Data Types
- Flow Control
- Data Structures
- Importing Modules
- Dependency Management
- Error Handling
- Logging
- Testing

>NOTE: This repository was created for an internal Python workshop at [AllCloud][2].

## What is Python?

![monty python](images/monty_python.jpg)

>Fun fact! Python is named after [Monty Python's Flying Circus][4]. The official Python docs are
>full of Monty Python references, jokes and easter eggs. By the way, if you don't know who Monty
>Python are, please stop reading this guide as you obviously have more important things to learn.

OK, back to reality. From the official Python [documentation][3]:

>Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

Let's break this down.

### Python is Interpreted

When you write code you are doing nothing more than editing **simple text files**. These text files
cannot be executed by the CPU inside your computer. The CPU speaks a very specific, low-level
language ("machine language") which is extremely difficult to work with for humans. Moreover, every
CPU type speaks a **different** machine language, so the Intel CPU inside your laptop cannot run
the same code as the ARM CPU inside your phone.

When you write code in C (or Go or Rust for that matter), you feed your code to a **compiler**,
which is simply a program that can read text files and generate files with machine language, or
**binary files**, from them.

When you write code in Python, on the other hand, your code is fed to an **interpreter**, which is
a program that **executes the code** instead of generating a binary file from it.

>NOTE: The above is not always true in the case of Python. I am presenting the most common case
>here on purpose to help convey the message.

### Python is Object-Oriented

In object-oriented programming you describe a real-world problem in your code using virtual
elements (called "objects") **which represent real things**, sometimes even physical things. For
example, you could create two objects which represent cars, and tell one of them to start the
engine:

    my_car = Car(color='red')
    my_other_car = Car(color='blue')
    my_car.start()

So now `my_car` is running and `my_other_car` is not.

### Python is High-Level

Generally speaking, the easier it is for a human to work with a programming language, the harder it
is for a computer to run the code. Nowadays, an hour of a programmer's work is usually way more
expensive than consuming a few more CPU cycles. That's why we don't do web development in C
(although it is perfectly possible to do so!).

Python puts the focus on **developer productivity** rather than on performance. This does not mean
you can't write high-performance code in Python, but -  again, generally speaking - Python apps
tend to be much slower than Java apps, Go apps or C apps.

**However**, the upside is that Python is **really easy to work with**. Its syntax is minimalist
(`public static void main(String[] args) {System.out.println("Java is minimalist, too!");}`), it
doesn't rely on [arcane characters][5] to do its job, it doesn't use parentheses and brackets when
they aren't needed (((((((([hi!][6])))))))) and you can feel free to forget as many semicolons as
you like!

### Python is Dynamic

The main thing you need to know for now is that we don't need to *tell* Python what type of a
variable we are creating, it figures it out on its own:

    my_string = "Ni!"
    my_number = 3

### What Python is Not?

**Python is not a program**. True, most Linux distributions come with an executable called
`python`. This is actually the most common Python **interpreter** called [CPython][7] (because it
is a program that is written in C). Python is a **language**, and CPython is just one Python
*implementation*. [There][8] [are][9] [many][10] [others][11].

And now for something completely different.

## 2 or 3?

3.

## Setting up Your Work Environment

In order to run Python code you will need a Python interpreter. You may already have a Python
interpreter installed on your machine. Any Python 3 release would do for this workshop.

Type `python` on your shell. If you have Python installed, you should see something like the
following:

    Python 3.6.5 (default, Apr 25 2018, 14:23:58)
    [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Notice the version (`Python 3.6.5` in the output above). If you get `Python 2.x.x`, try running
`python3`. If you still don't get a Python 3 interpreter, follow the instructions below.

### Mac Users

TL;DR: `brew install python`.

For detailed info, follow these great [instructions][12] from Kenneth Reitz.

>NOTE: If you are running OSX High Sierra and are having trouble getting Python 3 to work for you
>by default, take a look [here][15].

### Windows Users

You can get a Mac [here][13]. Or follow the instructions [here][[16].

### Linux Users

You probably don't need assistance, but in case you do - [there you go][14].

## Using the Python Interpreter

One of the nicest things about interpreted programming languages is that you can often work with
them interactively. Let's try the following:

Open your terminal, type `python` and hit Enter. Assuming you've [set up][17] your work
environment, you should get a prompt similar to the following:

    Python 3.6.5 (default, Apr 25 2018, 14:23:58)
    [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Now type `print('hi!')` and hit Enter.

    >>> print('hi!')
    hi!
    >>>

What do you know - it worked! You can also calculate stuff:

    >>> 3 + 5
    8
    >>>

You can assign values to variables and then use them:

    >>> print('Hello', name)
    Hello Bob
    >>>

As a matter of fact, you can type *any* Python expression into this shell and the interpreter will
execute it.

Now, while having an interactive shell is great for quick, small-scale ad-hoc tests, it is not very
comfortable for writing a lot of code.

[1]: https://github.com/boto/boto3
[2]: https://www.allcloud.io
[3]: https://www.python.org/doc/essays/blurb/
[4]: https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus
[5]: https://www.foo.be/docs/tpj/issues/vol4_3/tpj0403-0017.html
[6]: https://en.wikipedia.org/wiki/Scheme_(programming_language)
[7]: https://en.wikipedia.org/wiki/CPython
[8]: https://pypy.org/
[9]: http://www.jython.org/
[10]: http://pypyjs.org/
[11]: https://common-lisp.net/project/clpython/
[12]: http://docs.python-guide.org/en/latest/starting/install3/osx/
[13]: https://apple.com
[14]: http://docs.python-guide.org/en/latest/starting/install3/linux/
[15]: https://github.com/kennethreitz/python-guide/issues/895
[16]: http://docs.python-guide.org/en/latest/starting/install3/win/
[17]: #setting-up-your-work-environment
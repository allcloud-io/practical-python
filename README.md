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
- Using the Interactive Shell
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

>Fun fact: Python is named after the British comedy group [Monty Python][4].

![monty python][monty python]

From the official Python [documentation][3]:

>Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

Let's break this down.

### Python is Interpreted

When you write code you are doing nothing more than editing **simple text files**. These text files
cannot be executed by the CPU inside your computer. The CPU speaks a very specific, low-level
language ("machine language") which is extremely difficult to work with for humans. Moreover, every
CPU type speaks **a different machine language**, so the Intel CPU inside your laptop cannot run
the same code as your ARM CPU inside your phone.

When you write code in C (or Go or Rust for that matter), you feed your code into a **compiler**,
which is simply a program that can read text files and generate files with machine language, or
**binary files**, from them.

When you write code in Python, on the other hand, your code is fed to an **interpreter**, which is
a program that **executes the code** instead of generating a binary file from it.

>NOTE: There above is not always true in the case of Python. I am presenting the most common case
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

### What Python is Not?

TODO

[1]: https://github.com/boto/boto3
[2]: https://www.allcloud.io
[3]: https://www.python.org/doc/essays/blurb/

[monty python] images/monty_python.jpg
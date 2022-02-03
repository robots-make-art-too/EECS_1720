# Python intro

note: work-in-progress

## What is Python

Python is a very easy Programming Language. It’s like writing the code in the English Language.

Python is a general-purpose high-level Programming Language. 
  
1. general-purpose- As it can be used to build a web app, machine learning, desktop app, robotics, artificial intelligence, IoT, gaming, data Analysis
  
2. high-Level Programming Language- Assembly language is a low-level language and can interact with the hardware but is not human friendly. However Python, Java is a high- level programming language.

3. Python is a dynamically typed language. i.e., You need not declare the type of variable. It is assigned automatically based on the value that you store in the variable

### Features

Python has the following programming features, borrowed from different languages

- Functional Programming from C
- OOP from C++
- Scripting language feature from Perl and Shell Script
- Modular programming language

---

### What else is helpful about python?

- platform-independent- You can write the code once in any O.S and can run the code anywhere.

- portable- Portability means you write the code in one machine and then if you port the code to any other machine then it won't require any changes.

- interpreted Language- To run the program you need not compile the program

- extensible- Extensible feature in python refers that you can write some of your Python code in other languages like C or C++

- improve performance

- embedded: Python code can be embedded in any other programming language.

- extensive Library Support

---

## Python Versions

1. Python 3 backward _INCOMPATIBLE_ as it fixed problems in Python v2 (discontinued in 2020 - so we wont use it)
   - Some current Linux distributions and Macs still use 2.x as default

2. Many libraries developed for Python 2 are not compatible in Python 3. 

3. The developers of libraries used in Python 3 has good standards and have enhanced the Machine Learning and Deep Learning libraries.

### Take note of

(but only if you already know some python)

- Python 3 default storing of strings is Unicode
- Python 3 value of variables never changes whereas in 
- Python 2 value of the global variable will be changed while using it inside for-loop.
- Python 3 exceptions should be enclosed in parenthesis while Python 2 exceptions should be enclosed in notations.
- Python 3 offers Range() function to perform iterations whereas, In Python 2, the xrange() is used for iterations.


### Python 2

(advanced students)

Although, Python 2 is an old open source version here are where you still need to learn Python 2:

To become a DevOps engineer and you need to work with configurations management tools like puppet or ansible. Here, you need to work with both of these versions.
   - e.g., If your company's code is written in Python 2, you will have to learn to work with that
   - e.g., If your development team is working on a project that depends on specific third-party libraries or software which you are not able to port to Python 3, then Python 2 is the only option available for you.

### Python3

Here are prime reasons for using Python 3.x versions:

1. Python 3 supports modern techniques like AI, machine learning, and data science
2. Python 3 is supported by a large Python developer’s community. Getting support is easy.
3. It's easier to learn Python language compared to earlier versions.
4. Offers Powerful toolkit and libraries
5. Mixable with other languages

---

## Why Python

We saw some useful examples in class, but also:

- processing.py
- servers
- circuitpython

### CircuitPython 

Not this course but for sure Physical Programming and plenty of it in Digital Media

This is a programming language designed to simplify experimenting and learning to program on low-cost microcontroller boards (all those blinking LEDs, haptic controlls, mini displays, etc etc etc!)

--- 

## IDEs and VEs


Recall: What are IDEs and Code Editors?

An IDE is a software that consists of common developer tools into a single user-friendly GUI (Graphical User interface). An IDE majorly consists of a source code editor for writing software code, local build automation for creating a local build of the software like compiling computer source code. Lastly, it has a debugger, a program for testing other programs. An IDE can have many more features apart from these & those vary for each IDE.

Code editors are also software; it is like a text editor with some added functionalities. It is not an IDE as an IDE has many developer tools. Depending upon the language one codes on the editor, it highlights special keywords and gives some suggestions. Sublime Text, Atom, Visual Studio Code are some of the popular code editors. 


### IDE

- Pydev plugin for Eclipse - easy to leary, includes features like CPython, Jython..)
- Pycharm - debug and execute without external reqs, live ode verification
- Sublime - fast with few bugs (!), opens large files
- Visual Studio Code - DYK: can import keyboard shortcuts from other editors you use, like sublime
- IDLE - can execute single statments, debugger
- Spyder - rich suport, tools, documentation
- Thonny - adapted fro beginners


### VEs

(advanced students)

A Python virtual environment consists of two essential components: the Python interpreter that the virtual environment runs on and a folder containing third-party libraries installed in the virtual environment. 

These virtual environments are isolated from the other virtual environments, which means any changes on dependencies installed in a virtual environment don’t affect the dependencies of the other virtual environments or the system-wide libraries. 

Thus, we can create multiple virtual environments with different Python versions, plus different libraries or the same libraries in different versions.

NOTE: As a piece of advice for new Python programmers, always set up a separate virtual environment for each Python project, and install all the required dependencies inside it — never install packages globally.

---

## JSON

{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

Simple Python objects are translated to JSON according to a fairly intuitive conversion.

Python            JSON

dict              object
list, tuple       array
str               string
int, long, float  number
True              true
False             false
None              null

Next part is for advanced students:

What happens after a computer processes lots of information? It needs to take a data dump. Accordingly, the json library exposes the dump() method for writing data to files. There is also a dumps() method (pronounced as “dump-s”) for writing to a Python string.


## Examples from class

get links from website

resolution of image
rotate an image
resize an image

find files

use dates

password generator

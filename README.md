# Python
Complete Python Developer in 2020: Zero to Mastery Created by Andrei Neagoie

## Section 1: Introduction
- Course Outline
- Join Our Online Classroom!
- Discord Community

## Section 2: Python Introduction

### What Is A Programming Language?
- Source code (human readable)
  - => interpreter: goes line by line and executes it consecutively
  - => or compiler: takes code all at once, reads the entire file and then translates that to machine code.

### [Python Interpreter](https://www.python.org/)
- cypthon VM (virtual machine)

### How to Run Python Code
- Terminal
- Code Editors: sublime text, visual studio code
- IDEs: PyCharm, Spyder
- Notebooks: jupyter
- `python3`
- `exit()`
- `python main.py`

### Python 2 vs Python 3
- Python3 introduced in 2008
- [The Story of Python](https://www.youtube.com/watch?v=J0Aq44Pze-w)
- [Python 2 vs Python 3](https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/)
- [Another Article](https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)

### [Why So Many Languages](https://en.wikipedia.org/wiki/List_of_programming_languages)
- Languages have tradeoffs, so choose depending on purpose
- Python is great for developer code

### [ZTM Python Cheat Sheet](https://zerotomastery.io/courses/python/cheatsheet/?utm_source=udemy&utm_medium=coursecontent)

## Section 3: Python Basics

### Learning Python
- Terms
- Data Types
- Actions
- Best Practices


### Python Data Types
- Numbers
- [Math Functions](https://www.programiz.com/python-programming/modules/math)

### Developer Fundamentals I
- Learn a language by using it not by memorizing it.

### Operator Precedence

### Optional: bin() and complex

### Variables
- [Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)
- Best Practices
  - snake_case
  - start with lowercase or underscore
  - letters, numbers, underscores
  - case sensitive
  - don't overwrite keywords
  - CONSTANTS are CAPITALIZED

### Expressions vs Statements
- expressions: pieces of code that produce a value (right side of equation)
- statements: entire lines of code that perform an action

### Augmented Assignment Operator
- e.g., `+=`, `*=`

### Strings

### String Concatenation

### Type Conversion

### Escape Sequences
- `\` to make next char a string
- `\t` for a tab
- `\n` for a new line


### Formatted Strings
- f string `(f ...)` - recommended
- `.format()` still used from Python 2

### String Indexes
- access different parts of a string by its index

### Immutability
- once created, you cannot reassign part of a string

### Built-In Functions + Methods
- [Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Methods](https://www.w3schools.com/python/python_ref_string.asp)

### Booleans

### Developer Fundamentals II: Commenting Code
- [Writing Comments in Python](https://realpython.com/python-comments-guide/)

### Lists
- ordered sequence of objects
- like arrays in other languages
- List Slicing
- Lists are mutable
  - copying vs modifying

### Matrix
- an array with another array inside it [multi-dimensional]

### Dictionaries
- Also known as mappings or hash tables. They are key value pairs that DO NOT retain order
`dict` data type

### Developer Fundamentals III: Using Data Structures

### Dictionary Keys
- has to be immutable (a `list` cannot be a key because it can change)
- has to be unique, a repeated key will be overwritten

### Dictionary Methods

### Tuples
- immutable lists: e.g., children = ('Omi', 'SungOh')
- Tuple Methods
  - `count()`
  - `index()`

### Sets
- unordered collection of unique elements (no duplicates)
- [Python Set Methods](https://www.w3schools.com/python/python_ref_set.asp)

## Section 4: Python Basics II

### Conditional Logic
  - if
  - elif
  - else

### Indentation in Python

### Truthy vs Falsy
- [What is Truthy and Falsy?](https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false)

### Ternary Operator
`condition_if_true if condition else condition_if_false`

### Short Circuiting

### Logical Operators
- and, or, >, <, ==, !=, not, and not, etc.

### is (===) vs ==

### For Loops

### Iterables
- list
- dictionary
- tuple
- set
- string

### range(), enumerate()

### While Loops

### `break`, `continue`, `pass`

### Our First GUI: A Christmas Tree

### Developer Fundamentals IV: What is good code?
- clean
- readable
- predictable
- DRY - don't repeat yourself

### Functions
- `def` define a function
- should do one thing really well
- should return something

### Parameters and Arguments
- parameters define variables to pass into a function
- arguments are called (invoked) when running a function

### Default Parameters and Keyword Arguments
- assign a default parameter
- can use keyword arguments to explicitly define the values rather than positional arguments

### Return
- functions should `return` something

### Methods vs Functions
- `.method` has to be owned by something to the left of the period

### Docstrings: comment code inside of functions
```Python3
def test(a)
'''
Info: this function tests and prints param a
'''
  print()

test('!!!')
```

### Clean Code

### *args and **kwargs
- Rule order: params, *args, default parameters, **kwargs

### Scope - what variables do I have access to?
1. start with local
2. Parent of local?
3. Global
4. Built in Python functions'

### global keyword and nonlocal keyword
- `nonlocal` used to refer to the parent local
- generally write clean code and don't use these keywords

### Why Do We Need Scope
- garbage collection

### Python Exam: Testing Your Understanding
- [Test 1: 25 Questions](https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON)
- [Test 2: 51 Questions](https://www.w3schools.com/python/exercise.asp)

## Section 5: Developer Environment
- Code Editors: lightweight as they provide editors and linting
- IDEs are full-fledged environments
- Tools
  - Code Editors
    - Sublime Text
    - Visual Studio Code
  - IDEs
    - PyCharm
    - Spyder
  - Notebooks
    - jupyter

### Code Formatting - PEP (Python Enhancement Proposals) 8 (Style Guide for Python Code)

## Section 6: Advanced Python: Object Oriented Programming

### Object Oriented Programming
- a paradigm for structuring and writing our code
- modeling our code in terms of real world objects
- CLASS => instantiate instances
  - `class CamelCase:`

### Attributes and Methods

### __init__

### @classmethod and @staticmethod
- [Methods Differences](https://www.makeuseof.com/tag/python-instance-static-class-methods/)

### Developer Fundamentals V: Test Your Assumptions 

### Encapsulation 
- the binding of data and functions that manipulate that data into one big object to keep everything in this box for interaction 

### Abstraction 
- hiding information and giving access to only what's necessary

### Private vs Public Variables 
- no true private variables in Python 
- but convention to use underscore `_variable` to indicate it shouldn't be touched

### Inheritance 
- allows new objects to take on the characteristics of existing objects 
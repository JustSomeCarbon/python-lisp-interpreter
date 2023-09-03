This is a simple LISP interpreter written in Python

This interpreter is a simple implementation of the LISP language. Many parts of the original language are not available
in this application. This interpreter is able to handle simple arithmetic (such as addition, subtraction, multiplication,
and division) Logical expressions (such as greater than, less than, greater than or equal to, less than or equal to, equal
to, not equal to, and, or, and not), and a few simple functions (if conditionals, car, cdr, cons, sqrt, pow, !set, and define).

The interpreter was written as a required project for a class, and as such, was written in a smaller timeframe.
I have posted this project as an archive, so that I may recreate the project at a later date.
The following is the currently working functionality of the interpreter.  


Arithmetic:
- [X] addition, +
- [X] subtraction, -
- [X] multiplication, *
- [X] division, /

Logic:
- [X] greater than, >
- [X] less than, <
- [X] equal to, =
- [X] not equal to, !=
- [X] AND
- [X] OR
- [X] NOT

functions:
- [X] if conditional
- [X] car
- [X] cdr
- [X] cons
- [X] sqrt
- [X] pow
- [ ] defun
- [X] !set
- [X] define

Functionality:  
Variable definition is ready.  
Variable referencing within more complex expressions is ready  

TODO::  
Rectreate the project:
- [ ] re-write expression parser
- [ ] restructure how expression evaluation is cunducted (separate function calls from definitions)
- [ ] integrate function definitions within the interpreter

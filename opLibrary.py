#
# @author Noe Garcia
#
# @description This file contains all the built in functions for
#   the lisp interpreter.
# @built-in-functions: car, cdr, cons, sqrt pow, defun, !set
# @built-in-arithmetic: *, +, -, /
# @built-in-logic: <, >, =, !=, and, or, not
#

# LOGIC
def gthan(a, b):
    return int(a) > int(b)

def lthan(a, b):
    return int(a) < int(b)

def equal(a, b):
    return int(a) == int(b)

def notEqual(a, b):
    return int(a) != int(b)


# ARITHMETIC
def add(a, b):
    return int(a) + int(b)

def sub(a, b):
    return int(a) - int(b)
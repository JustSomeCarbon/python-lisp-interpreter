#
# @author Noe Garcia
#
# @description This file contains all the built in functions for
#   the lisp interpreter.
# @built-in-functions: car, cdr, cons, sqrt pow, defun, !set
# @built-in-arithmetic: *, +, -, /
# @built-in-logic: <, >, =, !=, and, or, not
#

import math


# LOGIC
def gthan(a, b):
    return int(a) > int(b)


def lthan(a, b):
    return int(a) < int(b)


def equal(a, b):
    return int(a) == int(b)


def notEqual(a, b):
    return int(a) != int(b)


def logicAnd(a, b):
    # evaluate exressions a and b
    if not isinstance(a, bool):
        if a.lower() == 'true':
            a = True
        else:
            a = False
    if not isinstance(b, bool):
        if b.lower() == 'true':
            b = True
        else:
            b = False

    return a and b


def logicOr(a, b):
    # evaluate exressions a and b
    if not isinstance(a, bool):
        if a.lower() == 'true':
            a = True
        else:
            a = False
    if not isinstance(b, bool):
        if b.lower() == 'true':
            b = True
        else:
            b = False

    return a or b


def logicNot(a):
    # evaluate expression a
    if not isinstance(a, bool):
        if a.lower() == 'true':
            a = True
        else:
            a = False

    return not a


# ARITHMETIC
def add(a, b):
    return int(a) + int(b)


def sub(a, b):
    return int(a) - int(b)


def mult(a, b):
    return int(a) * int(b)


def div(a, b):
    return float(a) / float(b)


# FUNCTIONS
def exprSqrt(a):
    return math.sqrt(float(a))


def exprPow(a, b):
    return math.pow(int(a), int(b))


# Error Handling
# things
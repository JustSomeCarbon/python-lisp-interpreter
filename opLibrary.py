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
        if a.lower() == 't':
            a = True
        else:
            a = False
    if not isinstance(b, bool):
        if b.lower() == 't':
            b = True
        else:
            b = False

    return a and b


def logicOr(a, b):
    # evaluate exressions a and b
    if not isinstance(a, bool):
        if a.lower() == 't':
            a = True
        else:
            a = False
    if not isinstance(b, bool):
        if b.lower() == 't':
            b = True
        else:
            b = False

    return a or b


def logicNot(a):
    # evaluate expression a
    if not isinstance(a, bool):
        if a.lower() == 't':
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
    if b == "0":
        return "Cannot divide by zero"
    return float(a) / float(b)


# BUILT IN FUNCTIONS
def carFunc(a):
    tmp = ""
    # return the first element of the list
    if a[1] == '(':
        # return the first list
        i = 2
        while a[i] != ")" and i < len(a):
            tmp += a[i]
            i += 1
        tmp = '(' + tmp + ')'
    else:
        i = 1
        while a[i] != " " and i < len(a):
            tmp += a[i]
            i += 1

    return tmp


def cdrFunc(a):
    n = 0
    # return everything but the first element of list
    # skip over the first element
    if a[1] == '(':
        n = 2
        i = 2
        while a[i] != ')' and i < len(a):
            n += 1
            i += 1
        n += 1
    else:
        n = 1
        i = 1
        while a[i] != " " and i < len(a):
            n += 1
            i += 1

    return '(' + a[n + 1:]


def consFunc(a, b):
    # concatenate a to the beginning of b
    # check for list
    if '(' in a:
        a = a[1:len(a) - 1]
    if '(' in b:
        b = b[1:len(b) - 1]

    return '(' + a + " " + b + ')'


def exprSqrt(a):
    return math.sqrt(float(a))


def exprPow(a, b):
    return math.pow(int(a), int(b))


# Error Handling
# things
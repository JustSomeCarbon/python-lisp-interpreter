#
# @author: Noe Garcia
#
# @description Holds all the functionality for the python lisp interpreter.
#

# imports
import sys

# GLOBAL FUNCTION STACKS
funcNames = []
funcDefs = []
# GLOBAL VARIABLE STACK
varNames = []

# GLOBAL OPERATIONS
logicOps = ["<", ">", "=", "!=", "and", "or", "not"]
arithOps = ["+", "-", "*", "/"]
builtOps = ["car", "cdr", "cons", "sqrt", "pow", "defun", "!set"]


# Takes in the string expression from the main function.
# @return array of expressions
def parseExpression(expStr):
    # define the empty array for the expression
    expr = []
    #print(expStr)

    # check character by index
    if expStr[0] != "(":
        expr.append("quit")
        return expr

    # parse expression
    i = 1
    length = len(expStr)
    tmp = ""
    while i < length:
        # recursively call parse for each recurring embedded expression
        if expStr[i] == "(":
            # push onto stack
            newExpr = expStr[i:]
            #print(expr)
            expr.append(parseExpression(newExpr))
            # update the index for scope
            #print(i)
            i += lookForTerminatingExpr(newExpr) - 1
        elif expStr[i] == ")":
            # return the expression
            return expr
        else:
            tmp = ""
            # check if the following is defined as an atom
            if expStr[i] == "'" and expStr[i + 1] == "(":
                n = lookForTerminatingExpr(expStr[i + 1:])
                end = i + n + 2
                print("found an atom. end:", end)
                # the following until the space is an atom
                while i < end and i < length:
                    tmp += expStr[i]
                    i += 1
                expr.append(tmp)
            # look to build the expression and push to the array
            elif expStr[i] != " " and i < length:
                while expStr[i] != " " and expStr[i] != ")" and i < length:
                    #print(i, len(expStr))
                    tmp += expStr[i]
                    #print(tmp)
                    i += 1
                # END OF WHILE
                expr.append(tmp)
                if expStr[i] == ")":
                    i -= 1
            # END OF IF/ELIF

        # iterate through
        i += 1
    ## END OF WHILE
    return expr
    #sys.exit("Error:: Parsing error, missing )")


# local function to help find the terminating parenthesis
# @return the index of terminating parentheses
def lookForTerminatingExpr(expStr):
    scope = 0
    n = 1
    while n < len(expStr):
        if expStr[n] == ")" and scope == 0:
            #print(n)
            return n
        elif expStr[n] == "(":
            scope += 1
        elif expStr[n] == ")" and scope != 0:
            scope -= 1
        n += 1
    print("Something went wrong!")
    return n


# Takes the expression array that was parsed before and
# looks to execute the expressions defined by the user
# @return result of expression as a string
def evaluation(exprList, index):

    # check the first expression given is a defined keyword
    if exprList[index] in logicOps:  # logic operations
        if exprList[index] == ">":
            print("greater than")
        if exprList[index] == "<":
            print("less than")
        if exprList[index] == "=":
            print("equal to")
        if exprList[index] == "!=":
            print("not equal to")
        if exprList[index] == "and":
            print("and op")
        if exprList[index] == "or":
            print("or op")
        if exprList[index] == "not":
            print("not op")

    elif exprList[index] in arithOps:  # arithmetic operations
        if exprList[index] == "+":
            print("addition")
        if exprList[index] == "-":
            print("subtraction")
        if exprList[index] == "*":
            print("multiplication")
        if exprList[index] == "/":
            print("division")

    elif exprList[index] in builtOps:  # built in functions
        if exprList[index] == "car":
            print("function car")
        if exprList[index] == "cdr":
            print("function cdr")
        if exprList[index] == "cons":
            print("function cons")
        if exprList[index] == "sqrt":
            print("function sqrt")
        if exprList[index] == "pow":
            print("function pow")
        if exprList[index] == "defun":
            print("function defun")
        if exprList[index] == "!set":
            print("function !set")

    # check if the first expression is a user defined function keyword
    if exprList[index] in funcNames:
        # user defined functions
        print("user defined functions")

    # check if the first expression is a user defined variable
    if exprList[index] in varNames:
        # user defined variables
        print("user defined variables")

    return 0


# END OF EVALUATION
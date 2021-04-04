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
            # look to build the expression and push to the array
            if expStr[i] != " " and i < length:
                while expStr[i] != " " and expStr[i] != ")" and i < length:
                    #print(i, len(expStr))
                    tmp += expStr[i]
                    #print(tmp)
                    i += 1
                # END OF WHILE
                expr.append(tmp)
                if expStr[i] == ")":
                    i -= 1
            # END OF IF

        # iterate through
        i += 1
    ## END OF WHILE
    sys.exit("Error:: Parsing error, missing )")


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
def commandHandler(exprList, index):
    # check the first expression given is a defined keyword
    if exprList[index] in logicOps:
        # logic operations
    elif exprList[index] in arithOps:
        # arithmetic operations
    elif exprList[index] in builtOps:
        # built in functions

    # check if the first expression is a user defined function keyword
    if exprList[index] in funcNames:
        # user defined functions

    # check if the first expression is a user defined variable
    if exprList[index] in varNames:
        # user defined variables
#
# @author: Noe Garcia
#
# @description Holds all the functionality for the python lisp interpreter.
#

# imports
import sys
import opLibrary

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
def parseExpression(expStr, depth):
    # store the depth
    retDepth = depth
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
            # add a depth
            depth += 1
            # push onto stack
            newExpr = expStr[i:]
            expr.append(parseExpression(newExpr, depth))  # i
            # update the index for scope
            #print(i)
            i += lookForTerminatingExpr(newExpr) - 1
        elif expStr[i] == ")":
            # return the expression
            if retDepth == depth:
                # print("returned:", expr)
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
    # print("EVAL::", exprList)
    result = 0

    # CHECK FOR RECURSIVE DEPTH
    # CHECK FOR BOUNDS
    if (index + 1) < len(exprList):
        if isinstance(exprList[index + 1], list):
            exprList[index + 1] = evaluation(exprList[index + 1], 0)
    if (index + 2) < len(exprList):
        if isinstance(exprList[index + 2], list):
            exprList[index + 2] = evaluation(exprList[index + 2], 0)
    # END OF CHECK
    # ARRAY INDEX UPDATED

    # check the first expression given is a defined keyword
    if exprList[index] in logicOps:  # logic operations
        if exprList[index] == ">":  # GREATER THAN
            # print("greater than")
            # call the greater than function
            result = opLibrary.gthan(exprList[index + 1], exprList[index + 2])

        if exprList[index] == "<":  # LESS THAN
            # print("less than")
            # call the less than function
            result = opLibrary.lthan(exprList[index + 1], exprList[index + 2])

        if exprList[index] == "=":  # EQUAL TO
            # print("equal to")
            # call the equal to function
            result = opLibrary.equal(exprList[index + 1], exprList[index + 2])

        if exprList[index] == "!=":  # NOT EQUAL
            # print("not equal to")
            # call the not equal to function
            result = opLibrary.notEqual(exprList[index + 1],
                                        exprList[index + 2])

        if exprList[index] == "and":  # AND
            print("and op")
        if exprList[index] == "or":  # OR
            print("or op")
        if exprList[index] == "not":  # NOT
            print("not op")

    elif exprList[index] in arithOps:  # arithmetic operations
        if exprList[index] == "+":  # ADDITION
            # print("addition")
            # call the addition function
            result = opLibrary.add(exprList[index + 1], exprList[index + 2])

        if exprList[index] == "-":  # SUBTRACTION
            # print("subtraction")
            # call the subtraction function
            result = opLibrary.sub(exprList[index + 1], exprList[index + 2])

        if exprList[index] == "*":
            # print("multiplication")
            # call the multiplication function
            result = opLibrary.mult(exprList[index + 1], exprList[index + 2])
        if exprList[index] == "/":
            # print("division")
            # call the division function
            result = opLibrary.div(exprList[index + 1], exprList[index + 2])

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

    return result


# END OF EVALUATION
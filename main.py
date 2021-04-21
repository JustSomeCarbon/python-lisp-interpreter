import functionModule
#import os


def main():
    # open result file
    file = open("./results.file", "a")
    op = "Welcome to the LISP interpreter!"
    print(op)
    file.write(op + "\n")

    usr = "init"

    while (usr != "(quit)"):
        usr = input("> ")
        result = "EOF"
        expr = functionModule.parseExpression(usr, 0)
        # print(expr)  # for parseExpression debugging
        if expr == []:
            print(">> NIL")
            continue
        if expr[0] != "(quit)":
            expr = functionModule.swapExpression(expr)
            # print(expr) # for swapExpression debugging
            result = functionModule.evaluation(expr, 0)
            print(">> ", result)
        file.write(">" + usr + "\n")
        file.write(">>" + str(result) + "\n")
    # END OF WHILE

    # close the file
    file.close()
    print("> bye")


if __name__ == "__main__":
    main()
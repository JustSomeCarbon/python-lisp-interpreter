import functionModule


def main():
    usr = "init"

    while (usr != "(quit)"):
        usr = input("> ")
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
    # END OF WHILE

    print("> bye")


if __name__ == "__main__":
    main()
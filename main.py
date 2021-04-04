import functionModule


def main():
    usr = "init"

    while (usr != "quit"):
        usr = input("> ")
        expr = functionModule.parseExpression(usr)
        print(">> ", expr)
    # END OF WHILE

    print("> bye")


if __name__ == "__main__":
    main()
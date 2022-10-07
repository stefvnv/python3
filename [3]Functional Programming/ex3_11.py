def main():
    printName("John")
    print()
    underline_decorator(printName)("John")
    print('\n')
    overline_decorator(underline_decorator(printName))("John")


def underline_decorator(func):
    def closure(n):
        func(n)
        print("=============")

    return closure


def overline_decorator(func):
    def closure(n):
        print("=============")
        func(n)


    return closure


def printName(name):
    print("Name=" + name)


main()

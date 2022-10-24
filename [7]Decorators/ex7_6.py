def main():
    printNames("John", "Joseph", "Lennon")
    print()
    printNames("John", "Joseph", "Michael", "Smith")
    print()
    printNames("John", "Joseph", "Michael", "Leo", "Jones")


def max_four_args_decorator(func):
    def closure(*args):
        if len(args) > 4:
            print("Only 4 Arguments Allowed")
        else:
            func(*args)
    return closure


@max_four_args_decorator
def printNames(*args):
    for el in args:
        print(el, end=' ')


main()

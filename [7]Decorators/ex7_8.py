def main():
    printNames("John", "Joseph", "Lennon")
    print()
    printNames("John", "Joseph", "Michael", "Smith")
    print()
    printNames("John", "Joseph", "Michael", "Leo", "Jones")


def max_args_decorator(max_args=4):
    def limit_args_decorator(func):
        def closure(*args):
            if len(args) > max_args:
                print("Only {0} Arguments Allowed".format(max_args))
            else:
                func(*args)

        return closure

    return limit_args_decorator


@max_args_decorator(3)
def printNames(*args):
    for el in args:
        print(el, end=' ')


main()

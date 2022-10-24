def main():
    print('\nName= ', end='')
    printName("Joan Smith")
    print()


def titleMr_decorator(func):
    def closure(n):
        print('Mr ', end='')
        func(n)

    return closure


def titleMs_decorator(func):
    def closure(n):
        print('Ms ', end='')
        func(n)

    return closure


def qualBSc_decorator(func):
    def closure(n):
        func(n)
        print(' Bsc', end='')

    return closure


@titleMs_decorator
@qualBSc_decorator
def printName(name):
    print(name, end='')


main()

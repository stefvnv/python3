def main():
    value1 = int(input('Enter Value1:'))
    value2 = int(input('Enter Value2:'))
    res = divide(value1, value2)
    print('Result = ', res)


def no_zero_decorator(func):
    def closure(v1, v2):
        if v1 == 0 or v2 == 0:
            print("Zero Arguments Not Allowed")
            return 0
        else:
            return func(v1, v2)

    return closure


@no_zero_decorator
def divide(x, y):
    return x / y


main()

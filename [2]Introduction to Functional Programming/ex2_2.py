import sys


def fun1():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    result1 = addInRange(a, b)
    print("\n Sum of Values {0} to {1} = {2}:".format(a, b, result1))


def addInRange(first, last):
    if first > last:
        return 0
    else:
        return first + addInRange(first + 1, last)


fun1()

import sys


def fun1():
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed: ", n)

    # use sys.argv to use command line arguments
    v1 = int(sys.argv[1])
    v2 = int(sys.argv[2])
    v3 = int(sys.argv[3])

    result = maximum(v1, v2, v3)
    print("\nmax of {0}, {1}, {2} = {3}".format(v1, v2, v3, result))


def maximum(value1, value2, value3):
    if value1 > value2 and value1 > value3:
        return value1
    elif value2 > value1 and value2 > value3:
        return value2
    else:
        return value3


fun1()

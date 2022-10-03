def main():
    list1 = [2, 3, 4, 5, 6, 7, 8, 9]
    print("The original list is : " + str(list1))
    result1 = hAdd(pDecr, list1.copy())
    print('Add Items after Decrement=', result1)
    result2 = hAdd(pStepEven, list1.copy())
    print('Add Items after Stepping Even Items=', result2)


pDecr = lambda a: a - 1

pStepEven = lambda a: (a + 1 if (a % 2 == 0) else a)


def hAdd(f, list):
    if len(list) == 0:
        return 0

    else:
        first = list.pop(0)
        return f(first) + hAdd(f, list)


main()

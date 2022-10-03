def main():
    list1 = [22, 3, 44, 5, 6, 77, 8, 9]
    print("The original list is : " + str(list1))
    result1 = hCount(pSingleDigit, list1.copy())
    print('Count Single Digit Items =', result1)
    result2 = hCount(pIsEven, list1.copy())
    print('Count Even Items =', result2)


pSingleDigit = lambda a: (a < 10)

pIsEven = lambda a: (a % 2 == 0)


def hCount(f, list):
    if len(list) == 0:
        return 0
    else:
        first = list.pop(0)
        if f(first):
            return 1 + hCount(f, list)
        else:
            return 0 + hCount(f, list)


main()

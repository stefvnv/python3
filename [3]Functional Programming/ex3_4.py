def main():
    list1 = [22, 3, 44, 5, 6, 77, 8, 9]
    print("The original list is : " + str(list1))
    result1 = hMax(pSingleDigit, list1.copy())
    print('Max Single Digit Items =', result1)
    result2 = hMax(pIsEven, list1.copy())
    print('Max Even Items =', result2)


pSingleDigit = lambda a: (a < 10)

pIsEven = lambda a: (a % 2 == 0)


def hMax(f, list):
    if len(list) == 0:
        return 0
    else:
        first = list.pop(0)
        if f(first) == True and first > hMax(f, list.copy()):
            return first
        else:
            return hMax(f, list.copy())


main()

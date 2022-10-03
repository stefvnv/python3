def main():
    list1 = [22, 3, 44, 5, 6, 77, 8, 9]
    print("The original list is : " + str(list1))
    result1 = hAdd2(pSingleDigit, list1.copy())
    print('Add Single Digit Items =', result1)
    result2 = hAdd2(pIsEven, list1.copy())
    print('Add Even Items =', result2)


pSingleDigit = lambda a: (a < 10)

pIsEven = lambda a: (a % 2 == 0)


def hAdd2(f, list):
    if len(list) == 0:
        return 0
    else:
        first = list.pop(0)
        if f(first):
            return first + hAdd2(f, list)
        else:
            return 0 + hAdd2(f, list)


main()

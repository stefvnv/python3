def main():
    val1 = int(input('Enter Value1: '))
    val2 = int(input('Enter Value2: '))
    val3 = int(input('Enter Value3: '))
    val4 = int(input('Enter Value4: '))
    result1 = hMax(pAdd, val1, val2, val3, val4)
    print('Max of Added Pairs=', result1)
    result2 = hMax(pSub, val1, val2, val3, val4)
    print('Max of Subtracted Pairs=', result2)


pAdd = lambda a, b: a + b
pSub = lambda a, b: a - b


def hMax(f, a, b, c, d):
    val1 = f(a, b)
    val2 = f(c, d)

    if val1 > val2:
        return val1
    else:
        return val2


main()

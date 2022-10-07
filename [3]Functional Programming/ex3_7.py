def main():
    list1 = [[2, 9], [4, 3, 7, 1], [1, 8, 9], [2, 7, 6]]
    print("List1 : " + str(list1))
    result4 = hCount(pAllSingleDigits, list1.copy())
    print('hCount AllSingles=', result4)
    list2 = [[2, 9], [4, 3, 17, 1], [1, 8, 9], [2, 17, 6]]
    print("List2 : " + str(list2))
    result5 = hCount(pAllSingleDigits, list2.copy())
    print('hCount AllSingles =', result5)


def hCount(f, list):
    if len(list) == 0:
        return 0
    else:
        first = list.pop(0)
        if f(first.copy()):
            return 1 + hCount(f, list.copy())
        else:
            return 0 + hCount(f, list.copy())


pAdd = lambda list: (0 if len(list) == 0 else list.pop(0) + pAdd(list))

pCount = lambda list: (0 if len(list) == 0 else 1 + pCount(list[1:]))

pMax = lambda list: (0 if len(list) == 0 else
                     list[0] if list[0] > pMax(list.copy()[1:])
                     else pMax(list[1:]))


def pCountZeros(list):
    if len(list) == 0:
        return 0
    else:
        first = list.pop(0)
        if first == 0:
            return 1 + pCountZeros(list)
        else:
            return 0 + pCountZeros(list)


def pAllSingleDigits(list):
    if len(list) == 0:
        return True
    else:
        first = list.pop(0)
        if 0 < first < 10:
            return pAllSingleDigits(list)
        else:
            return False


main()

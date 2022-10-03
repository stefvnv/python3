def main():
    list1 = [[2, -2], [4, -4, 7], [], [2, 0, 6]]
    print("List : " + str(list1))
    result4 = hCountZeros(pAdd, list1.copy())
    print('hCountZeros Add =', result4)


def hCountZeros(f, list):
    if len(list) == 0:
        return 0
    else:
        first = list.pop(0)
        if f(first) == 0:
            return 1 + hCountZeros(f, list)
        else:
            return 0 + hCountZeros(f, list)


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


main()

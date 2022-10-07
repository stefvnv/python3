def main():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    new_list = list(hmyExclude(lambda x: x % 2 == 0, lambda x: x > 7, my_list.copy()))

    print(my_list)
    print('Exclude Even Items and >7 items')
    print(new_list)


def hmyExclude(f1, f2, list):
    for el in list:
        if not (f1(el) or f2(el)):
            yield el


main()

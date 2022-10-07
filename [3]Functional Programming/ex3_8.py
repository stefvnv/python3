def main():
    my_list = [1, 2, 3, 4, 5, 6]

    new_list = list(hmyMap(lambda x: (x + 1), my_list.copy()))

    print(my_list)
    print(new_list)


def hmyMap(f, list):
    for el in list:
        yield f(el)


main()

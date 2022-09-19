def main():
    val1 = int(input('Enter Value: '))
    val2 = int(input('Enter Value: '))
    val3 = int(input('Enter Value: '))
    result = max(val1, val2, val3)
    print('Max= {0}'.format(result))


def max(x, y, z):
    result = 0

    if x > x > z:
        result = x

    elif y > x and y > z:
        result = y

    else:
        result = z

    return result


main()

class Calculate:

    @staticmethod
    def add(*args):
        result = 0

        for el in args:
            result += el
        return result

    @staticmethod
    def product(*args):
        result = 1

        for el in args:
            result *= el
        return result

    @staticmethod
    def maximum(*args):
        result = 0

        if len(args) > 0:
            result = args[0]

        for el in args:
            if el > result:
                result = el

        return result


def main():
    value1 = int(input('Enter Value1: '))
    value2 = int(input('Enter Value2: '))
    value3 = int(input('Enter Value3: '))
    value4 = int(input('Enter Value4: '))
    print('\nAdd {0}, {1}, {2} = {3}'.format(value1, value2, value3, Calculate.add(value1, value2, value3)))
    print('Add {0}, {1}, {2}, {3} = {4}'.format(value1, value2, value3, value4,
                                                Calculate.add(value1, value2, value3, value4)))
    print('Multiply {0}, {1} = {2}'.format(value1, value2, Calculate.product(value1, value2)))
    print('Max {0}, {1}, {2}, {3} = {4}'.format(value1, value2, value3, value4,
                                                Calculate.maximum(value1, value2, value3, value4)))


main()

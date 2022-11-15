from abc import ABC, abstractmethod


class MyList(ABC):

    def __init__(self, a, b):
        self._first = a
        self._second = b

    @abstractmethod
    def add(self):
        return self._first + self._second

    @abstractmethod
    def print(self):
        pass


class Pair(MyList):

    def __init__(self, a, b):
        MyList.__init__(self, a, b)

    def add(self):
        return self._first + self._second

    def print(self):
        print('Pair ({0},{1})'.format(self._first, self._second))


class Treble(MyList):

    def __init__(self, a, b, c):
        MyList.__init__(self, a, b)
        self._third = c

    def add(self):
        return self._first + self._second + self._third

    def print(self):
        print('Treble ({0},{1},{2})'.format(self._first, self._second, self._third))


class Quad(MyList):

    def __init__(self, a, b, c, d):
        MyList.__init__(self, a, b)
        self._third = c
        self._fourth = d

    def add(self):
        return self._first + self._second + self._third + self._fourth

    def print(self):
        print('Quad ({0},{1},{2},{3})'.format(self._first, self._second, self._third, self._fourth))


def main():
    pair1 = Pair(2, 3)
    quad1 = Quad(3, 4, 5, 6)
    treble1 = Treble(3, 4, 5)
    pair2 = Pair(6, 4)
    list = [pair1, quad1, treble1, pair2]
    print('List of Objects')
    print('===============')
    for el in list:
        el.print()
        print('Sum=', el.add())
        print()


main()

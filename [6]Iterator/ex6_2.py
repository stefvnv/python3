from abc import abstractmethod, ABC


class Iterator(ABC):
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Container(ABC):
    @abstractmethod
    def getIterator(self) -> Iterator:
        pass


class Number(Container, Iterator):
    def __init__(self, number):
        self.__number = number
        self.__index = 0

    def toString(self):
        return str(self.__number)

    def getIterator(self):
        return Number(self.__number)

    def hasNext(self):
        return self.__index < len(self.toString())

    def next(self):
        myNumber = self.toString()
        res = int(myNumber[self.__index])
        self.__index += 1
        return res

    def printDetails(self):
        print('\nNumber Details:')
        print('-----------------')
        print('Number= ', self.__number)


def main():
    newNumber = input('Enter Long Number: ')
    n = Number(newNumber)
    n.printDetails()

    sumDigits = getSumDigits(n)
    print('Sum of Digits = ', sumDigits)

    target = int(input("Enter Digit to search for : "))
    occurs = getDigitOccurs(n, target)
    print(target, ' occurs ', occurs, ' times in ', newNumber)


def getSumDigits(n):
    value = n.getIterator()
    total = 0
    while value.hasNext():
        digit = value.next()
        total += digit
    return total


def getDigitOccurs(s, target):
    value = s.getIterator()
    count = 0
    while value.hasNext():
        digit = value.next()
        if (digit == target):
            count += 1
    return count


main()

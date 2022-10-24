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


class Student(Container, Iterator):
    def __init__(self, name, m1, m2, m3, m4):
        self.__name = name
        self.__mark1 = m1
        self.__mark2 = m2
        self.__mark3 = m3
        self.__mark4 = m4
        self.__index = 0

    def toList(self):
        return [self.__mark1, self.__mark2, self.__mark3, self.__mark4]

    def getIterator(self):
        return Student(self.__name, self.__mark1, self.__mark2, self.__mark3, self.__mark4)

    def hasNext(self):
        return self.__index < 4

    def next(self):
        myList = self.toList()
        res = myList[self.__index]
        self.__index += 1
        return res

    def printDetails(self):
        print('\nStudent Details:')
        print('-----------------')
        print('Name= ', self.__name)
        print('Marks= ', self.__mark1, self.__mark2, self.__mark3, self.__mark4)


def main():
    newStudent = input('Enter Name:')
    allResults = input('Enter 4 exam marks seperated by a space:')
    marks = allResults.split()
    s = Student(newStudent, int(marks[0]), int(marks[1]), int(marks[2]), int(marks[3]))
    s.printDetails()

    avgMark = getAverageMark(s)
    print('Average Mark= ', avgMark)

    highMark = getHighMark(s)
    print('Best Mark= ', highMark)


def getAverageMark(s):
    value = s.getIterator()
    total = 0
    while value.hasNext():
        mark = value.next()
        total += mark
    return total / 4


def getHighMark(s):
    value = s.getIterator()
    highest = 0
    while value.hasNext():
        mark = value.next()
        if mark > highest:
            highest = mark
    return highest


main()

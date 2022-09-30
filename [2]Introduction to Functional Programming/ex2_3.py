import sys


class Student:
    def __init__(self, n, m):
        self.__name = n
        self.__mark = m

    def myPrint(self):
        print('Student=', self.__name, self.__mark)

    def readName(self):
        return self.__name

    def readMark(self):
        return self.__mark


def fun1():
    s1 = Student('Jones', 47)
    s2 = Student('Shine', 66)
    s3 = Student('White', 55)
    s4 = Student('Smith', 34)
    s5 = Student('Peters', 44)
    list = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5}
    result = sumAllMarks(list)  # return 0 if not in list
    print('Sum of All Marks = {0}'.format(result))


def sumAllMarks(list):
    if len(list) == 0:
        return 0
    else:
        student = list.popitem()[1]

        mark = student.readMark()

        return mark + sumAllMarks(list)


fun1()

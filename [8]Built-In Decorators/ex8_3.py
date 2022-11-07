class DataList:

    def __init__(self, list):
        self.__list = list

    @classmethod
    def createDataArgs(cls, *args):
        my_list = list(args)
        return cls(my_list)

    @classmethod
    def createDataNumber(cls, number):
        my_list = list(map(int, str(number)))
        return cls(my_list)

    def addData(self):
        result = 0
        for el in self.__list:
            result += el
        return result

    def printData(self):
        print('\nList= {0}'.format(self.__list))


def main():
    list1 = [3, 2, 1, 5, 7]
    d1 = DataList(list1)
    d1.printData()
    print('sum=', d1.addData())

    d2 = DataList.createDataArgs(2, 3, 4, 5, 6)
    d2.printData()
    print('sum=', d2.addData())

    d3 = DataList.createDataNumber(12342)
    d3.printData()
    print('sum=', d3.addData())


main()

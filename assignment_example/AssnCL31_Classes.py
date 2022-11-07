class Company:

    def __init__(self, name,  location):
        # private variables
        self.__name = name
        self.__headQuarters = location

    def readName(self):
        return self.__name

    def readHeadquarters(self):
        return self.__headQuarters

    def updateQuarters(self, location):
        self.__headQuarters = location

#---------------------------------------------

class Product:

    def __init__(self, name, price, company, location):
        # private variables
        self.__name = name
        self.__price = price
             # aggregation
        self.__manufacturer = Company(company, location)
        self.__ordered = 0
        self.__available = True

    def readAvailable(self):
        return self.__available

    def markAvailable(self):
        self.__available = True

    def markUnavailable(self):
        self.__available = False

    def readName(self):
        return self.__name

    def readPrice(self):
        return self.__price

    def setPrice(self, newPrice):
        self.__price = newPrice

    def stepOrdered(self):
        if (self.__available==True):
            self.__ordered += 1

    def readOrdered(self):
        return self.__ordered

    def readCompany(self):
        return self.__manufacturer.readName()

    def readHeadquarters(self):
        return self.__manufacturer.readHeadquarters()

    # Polymorphic Methods

    def readType(self):
        return ''

    def readDescriptionPart1(self):
        return ''

    def readDescriptionPart2(self):
        return ''

    def readDescriptionPart3(self):
        return ''



    #--------------------------------------------

class Car(Product):

    def __init__(self, name, price, company, location,
                 engine, seating, doors):
        super().__init__(name, price, company, location)
        self.__engine = engine
        self.__seating = seating
        self.__doors = doors

    def readType(self):
        return 'Car'

    def readDescriptionPart1(self):
        return 'Engine (CC) : ' + str(self.__engine)

    def readDescriptionPart2(self):
        return 'Seats : ' + str(self.__seating)

    def readDescriptionPart3(self):
        return str(self.__doors) + ' Door '


    #--------------------------------------------

class Laptop(Product):

    def __init__(self, name, price, company, location,
                 ram, processor, screensize):
        super().__init__(name, price, company, location)
        self.__RAM = ram
        self.__processor = processor
        self.__screensize = screensize

    def readType(self):
        return 'Laptop'

    def readDescriptionPart1(self):
        return 'RAM : ' + str(self.__RAM)

    def readDescriptionPart2(self):
        return 'Processor : ' + str(self.__processor)

    def readDescriptionPart3(self):
        return 'Screen : ' + str(self.__screensize)


    #--------------------------------------------

class Book(Product):

    def __init__(self, name, price, company, location,
                 topic, author, type):
        super().__init__(name, price, company, location)
        self.__topic = topic
        self.__author = author
        self.__type = type

    def readType(self):
        return 'Book'

    def readDescriptionPart1(self):
        return 'Topic : ' + str(self.__topic)

    def readDescriptionPart2(self):
        return 'Author : ' + str(self.__author)

    def readDescriptionPart3(self):
        return 'Genre: ' + str(self.__type)

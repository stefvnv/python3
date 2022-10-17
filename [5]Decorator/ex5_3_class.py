from abc import abstractmethod, ABC


class Book(ABC):
    def __init__(self, title, ISBN, weight, price):
        self._title = title
        self._ISBN = ISBN
        self._weight = weight
        self._price = price

    def getTitle(self):
        return self._title

    def getISBN(self):
        return self._ISBN

    def getWeight(self):
        return self._weight

    def getPrice(self):
        return self._price

    @abstractmethod
    def getDeliveryPrice(self):  # After Discount
        pass

    @abstractmethod
    def getBookType(self):  # Normal, Heavy ,VeryHeavy
        pass

    def updatePrice(self, price):
        self._price = price


# ------------------------------------------------------

class NormalBook(Book):

    def __init__(self, title, ISBN, weight, price):
        super().__init__(title, ISBN, weight, price)

    def getDeliveryPrice(self):
        return 5

    def getBookType(self):  # Normal, Heavy ,VeryHeavy
        return "Normal"


class HeavyBook(Book):

    def __init__(self, title, ISBN, weight, price):
        super().__init__(title, ISBN, weight, price)

    def getDeliveryPrice(self):
        return 10

    def getBookType(self):  # Normal, Heavy ,VeryHeavy
        return "Heavy"


class VeryHeavyBook(Book):

    def __init__(self, title, ISBN, weight, price):
        super().__init__(title, ISBN, weight, price)

    def getDeliveryPrice(self):
        return 15

    def getBookType(self):  # Normal, Heavy ,VeryHeavy
        return "Very Heavy"


# --------------------Student Factory---------

class BookFactory:
    def getBook(self, title, ISBN, weight, price):

        if weight <= 300:
            return NormalBook(title, ISBN, weight, price)
        elif 300 < weight < 400:
            return HeavyBook(title, ISBN, weight, price)
        else:
            return VeryHeavyBook(title, ISBN, weight, price)


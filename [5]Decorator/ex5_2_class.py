from abc import abstractmethod, ABC


class Customer(ABC):

    def __init__(self, name, age, priority, price):
        self._name = name
        self._age = age
        self._priority = priority
        self._price = price

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getPriority(self):
        return self._priority

    def getGrossPrice(self):
        return self._price

    @abstractmethod
    def getNetPrice(self):  # After Discount
        pass

    @abstractmethod
    def getCustomerType(self):  # Priority, Regular, Child
        pass

    def updatePrice(self, price):
        self._price = price


# ------------------------------------------------------


class RegularCustomer(Customer):

    def __init__(self, name, age, priority, price):
        super().__init__(name, age, priority, price)

    def getNetPrice(self):
        return self._price

    def getCustomerType(self):  # Priority, Regular, Child
        return "Regular"


class ChildCustomer(Customer):

    def __init__(self, name, age, priority, price):
        super().__init__(name, age, priority, price)

    def getNetPrice(self):

        adjPrice = int(self._price * 0.5)
        if adjPrice > 100:
            return 100
        else:
            return adjPrice

    def getCustomerType(self):  # Priority, Regular, Child
        return "Child"


class PriorityCustomer(Customer):

    def __init__(self, name, age, priority, price):
        super().__init__(name, age, priority, price)

    def getNetPrice(self):

        adjPrice = int(self._price + 10)
        if adjPrice > 100:
            return 100
        else:
            return adjPrice

    def getCustomerType(self):  # Priority, Regular, Child
        return "Priority"


class CustomerFactory:
    def getCustomer(self, name, age, priority, price):

        if age < 17:
            if priority == True:
                return PriorityCustomer(name, age, priority, price)
            return ChildCustomer(name, age, priority, price)
        else:
            if priority == True:
                return PriorityCustomer(name, age, priority, price)
            return RegularCustomer(name, age, priority, price)

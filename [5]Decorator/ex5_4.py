def main():
    newName = input('Enter new Name:')
    # d1=Display(newName)
    # d1=UnderLine(Display(newName))
    # d1=OverLine(Display(newName))
    # d1=UnderLine(OverLine(Display(newName)))

    # **************************************
    factory = DisplayFactory()
    d1 = factory.getDisplay(newName)
    # **************************************

    option = menu()
    print()
    while option != 3:
        if option == 1:
            d1.printName()
        elif option == 2:
            newName = input('Enter new Name:')
            # d1.updateName(newName)
            # **********************************
            d1 = factory.getDisplay(newName)
            # *******************************
        option = menu()
        print()


def menu():
    print("\nMenu ")
    print("--------------")
    print("1.  print Name")
    print("2.  Change Name")
    print("3. Exit")
    result = int(input('Enter Choice:'))
    return result


# *****************************
class DisplayFactory:
    def getDisplay(self, name):
        if len(name) <= 5:
            return Display(name)
        elif len(name) >= 10:
            return OverLine(UnderLine(Display(name)))
        else:
            return UnderLine(Display(name))


# ******************************
class Display:
    def __init__(self, nm):
        self._name = nm

    def printName(self):
        print("Name= ", self._name)

    def updateName(self, nm):
        self._name = nm


class Decorator(Display):

    def __init__(self, dd):
        super().__init__("")
        self._display = dd


# OverLine Decorator
class OverLine(Decorator):

    def __init__(self, dd):
        super().__init__(dd)

    def printName(self):
        print("=================")
        self._display.printName()

    def updateName(self, nm):
        self._display.updateName(nm)


# UnderLine Decorator
class UnderLine(Decorator):

    def __init__(self, dd):
        super().__init__(dd)

    def printName(self):
        self._display.printName()
        print("=================")

    def updateName(self, nm):
        self._display.updateName(nm)


main()

# Solution

# Decorator

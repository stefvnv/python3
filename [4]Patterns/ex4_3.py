import self as self


def main():
    d1 = Display("Athlone")

    # d1=UnderLine(Display("Athlone"))
    # d1=OverLine(Display("Athlone"))
    d1 = UnderLine(OverLine(Display("Athlone")))

    option = menu()
    print()
    while option != 3:
        if option == 1:
            d1.printName()
        elif option == 2:
            newName = input('Enter new Name:')
            d1.updateName(newName)
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


class Display:
    def __init__(self, nm):
        self._name = nm

    def printName(self):
        print("Name= ", self._name)

    def updateName(self, nm):
        self._name = nm


class Decorator(Display):
    def __init__(self, display):
        super().__init__(0)
        self._display = display


class OverLine(Decorator):
    def __init__(self, dd):
        super().__init__(dd)

    def printName(self):
        print("=============")
        self._display.printName()

    def updateName(self, nm):
        self._display.updateName(nm)


class UnderLine(Decorator):
    def __init__(self, dd):
        super().__init__(dd)

    def printName(self):
        self._display.printName()
        print("=============")

    def updateName(self, nm):
        self._display.updateName(nm)


main()

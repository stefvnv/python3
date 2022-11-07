class Account():
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__accounts = 0
        self.__accounts += 1
        self.__number = 2000 + self.__accounts

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def printDetails(self):
        print('\nAccount: {0}'.format(self.__name))
        print('Balance: {0}'.format(self.__balance))

    def readNumber(self):
        return self.__number


def main():
    list = [Account('JB', 500), Account('MJ', 200), Account('PJ', 1000)]
    for el in list:
        el.printDetails()
        print('Number: {0}'.format(el.readNumber()))
        # print('Number of Accounts: {0}'.format(Account.readNumberOfAccounts()))

    newel = Account('MP', 200)
    newel.printDetails()
    print('Number: {0}'.format(newel.readNumber()))
    # print('Number of Accounts: {0}'.format(Account.readNumberOfAccounts()))


main()

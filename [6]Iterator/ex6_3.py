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


class Sentence(Container, Iterator):
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__index = 0

    def toList(self):
        result = self.__sentence.split()
        return result

    def getIterator(self):
        return Sentence(self.__sentence)

    def hasNext(self):
        return self.__index < len(self.toList())

    def next(self):
        myList = self.toList()
        res = myList[self.__index]
        self.__index += 1
        return res

    def printDetails(self):
        print('\nSentence Details:')
        print('-----------------')
        print('Sentence= ', self.__sentence)


def main():
    newSentence = input('Enter Sentence : ')
    s = Sentence(newSentence)
    s.printDetails()

    print('\nList of Words = ')
    printWords(s)

    target = input("\nEnter Word to search for : ")
    result = searchWord(s, target)
    if result == True:
        print(target, ' occurs in Sentence -      ', newSentence)
    else:
        print(target, ' does not occur in Sentence -       ', newSentence)


def printWords(n):
    value = n.getIterator()
    while value.hasNext():
        word = value.next()
        print(word)


def searchWord(s, target):
    value = s.getIterator()
    result = False
    while value.hasNext():
        word = value.next()
        if word.lower() == target.lower():
            result = True
    return result


main()

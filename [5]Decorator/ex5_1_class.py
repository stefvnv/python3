from abc import abstractmethod, ABC


class Student(ABC):

    def __init__(self, name, age, mark):
        self._name = name
        self._age = age
        self._mark = mark

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getMark(self):
        return self._mark

    @abstractmethod
    def getAdjustedMark(self):
        pass

    def updateMark(self, mark):
        self._mark = mark


# ------------------------------------------------------

class OldStudent(Student):

    def __init__(self, name, age, mark):
        super().__init__(name, age, mark)

    def getAdjustedMark(self):
        adjMark = int(self._mark * 1.1)
        if adjMark > 100:
            return 100
        else:
            return adjMark


class RegularStudent(Student):

    def __init__(self, name, age, mark):
        super().__init__(name, age, mark)

    def getAdjustedMark(self):
        return self._mark


class MatureStudent(Student):

    def __init__(self, name, age, mark):
        super().__init__(name, age, mark)

    def getAdjustedMark(self):
        adjMark = int(self._mark * 1.05)
        if adjMark > 100:
            return 100
        else:
            return adjMark


class EvenOlderStudent(Student):

    def __init__(self, name, age, mark):
        super().__init__(name, age, mark)

    def getAdjustedMark(self):
        adjMark = int(self._mark * 1.2)
        if adjMark > 100:
            return 100
        else:
            return adjMark


# --------------------Student Factory---------

class StudentFactory:
    def getStudent(self, name, age, mark):
        if age >= 70:
            return EvenOlderStudent(name, age, mark)
        elif age >= 65:
            return OldStudent(name, age, mark)
        elif 50 < age < 64:
            return MatureStudent(name, age, mark)
        elif age < 50:
            return RegularStudent(name, age, mark)

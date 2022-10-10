from tkinter import messagebox


class Counter:

    def __init__(self, val):
        self.__value = val
        self._message = ''

    def getValue(self):
        return self.__value

    def increment(self):
        self.__value += 1

    def decrement(self):
        self.__value -= 1

    def writeMessage(self, msg):
        self._message = msg

    def readMessage(self):
        return self._message


# ------------end of class definition------------------
# Decorator

class Decorator(Counter):

    def __init__(self, counter):
        super().__init__(0)
        self._counter = counter


class UpperLimit(Decorator):

    def __init__(self, counter):
        super().__init__(counter)

    def getValue(self):
        return self._counter.getValue()

    def increment(self):
        if self._counter.getValue() == 20:
            self.writeMessage("UpperLimit Reached")
        else:
            self._counter.increment()

    def decrement(self):
        self._counter.decrement()

    def writeMessage(self, msg):
        self._counter.writeMessage(msg)

    def readMessage(self):
        return self._counter.readMessage()


class LowerLimit(Decorator):

    def __init__(self, counter):
        super().__init__(counter)

    def getValue(self):
        return self._counter.getValue()

    def increment(self):
        self._counter.increment()

    def decrement(self):
        if self._counter.getValue() == 0:
            self.writeMessage("Already 0")
        else:
            self._counter.decrement()

    def writeMessage(self, msg):
        self._counter.writeMessage(msg)

    def readMessage(self):
        return self._counter.readMessage()


class Warn(Decorator):

    def __init__(self, counter):
        super().__init__(counter)

    def getValue(self):
        return self._counter.getValue()

    def increment(self):
        if 16 < self._counter.getValue() < 19:
            self._counter.increment()
            self.writeMessage("WARNING near 20")
        else:
            self._counter.increment()

    def decrement(self):
        if 1 < self._counter.getValue() < 4:
            self._counter.decrement()
            self.writeMessage("WARNING near 0")
        else:
            self._counter.decrement()

    def writeMessage(self, msg):
        self._counter.writeMessage(msg)

    def readMessage(self):
        return self._counter.readMessage()
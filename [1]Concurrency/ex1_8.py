from random import randint
from threading import *
import time
import sys


# ================================

class NumberStore:

    def __init__(self):
        self.contents = 0
        self.available = False
        self.lock1 = RLock()
        self.lock2 = RLock()
        self.event = Event()

    def get(self):
        self.lock1.acquire()
        while not self.available:
            self.event.wait()
        self.available = False
        self.event.set()
        self.lock1.release()
        return self.contents

    def put(self, value):
        self.lock2.acquire()
        while self.available:
            self.event.wait()
        self.contents = value

        self.available = True
        self.event.set()
        self.lock2.release()


# ==========================================

class Producer(Thread):

    def __init__(self, ns, n):
        Thread.__init__(self)
        self.store = ns
        self.number = n

    def run(self):
        for i in range(1, 10):
            self.store.put(i)
            # print("Producer #", self.number)
            time.sleep(randint(1, 5))


class Consumer(Thread):

    def __init__(self, ns, n):
        Thread.__init__(self)
        self.store = ns
        self.number = n

    def run(self):
        value = 0
        for i in range(1, 10):
            value = self.store.get()
            sys.stdout.write("Consumer #" + str(self.number) + " got: " + str(value) + '\n')
            # print("Consumer #", self.number, " got: ", value)
            time.sleep(randint(1, 5))


def main():
    ns = NumberStore()
    p = Producer(ns, 1)
    c = Consumer(ns, 1)

    c.start()
    p.start()


main()

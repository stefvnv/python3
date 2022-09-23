from threading import *
import time
import sys


def main():
    d1 = Incrementer_1_9()
    d2 = Decrementer_9_1()

    # change from change to start
    d1.start()
    d2.start()


# extend Thread class
class Incrementer_1_9(Thread):

    def run(self):
        for i in range(1, 10):
            sys.stdout.write('Increment_1_9:    ' + str(i) + "\n")
            time.sleep(1)


# extend Thread class
class Decrementer_9_1(Thread):

    def run(self):
        for i in range(9, 0, -1):
            sys.stdout.write('Decrement_9_1:     ' + str(i) + "\n")
            time.sleep(1)


main()

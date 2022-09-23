from threading import *
import time
import sys


def main():
    d1 = Display1_5()
    d2 = Display6_10()

    # change from display to start
    d1.start()
    d2.start()


# extend Thread class
class Display1_5(Thread):

    # change from display to run
    def run(self):
        for i in range(1, 6):
            sys.stdout.write('display1_5 ' + str(i) + "\n")
            time.sleep(1)


# extend Thread class
class Display6_10(Thread):

    # change from display to run
    def run(self):
        for i in range(6, 11):
            sys.stdout.write('display6_10 ' + str(i) + "\n")
            time.sleep(1)


main()

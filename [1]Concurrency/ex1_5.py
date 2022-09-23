from threading import *
import time
import sys

Res = 0

# add lock
lock = Lock()


def main():
    global Res
    t1 = Thread(target=step1)
    t2 = Thread(target=step2)
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    print('Final Value: ', Res)


def step1():

    # add global lock
    global Res, lock

    # add acquire
    lock.acquire()

    localVal1 = Res
    for i in range(1, 101):
        localVal1 += 1
        time.sleep(0.02)
    Res = localVal1

    # add release
    lock.release()


def step2():

    # add global lock
    global Res, lock

    # add acquire
    lock.acquire()

    localVal2 = Res
    for i in range(1, 101):
        localVal2 += 2
        time.sleep(0.02)
    Res = localVal2

    # add release
    lock.release()


main()

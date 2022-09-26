from threading import *
import time

value = 0
lock = Lock()


def main():
    global value
    t1 = Thread(target=increment)
    t1.start()
    t2 = Thread(target=increment)
    t2.start()

    # joins go here
    t1.join()
    t2.join()

    print('\nValue=', value)


def increment():
    global value, lock
    lock.acquire()
    tempValue = value + 1
    time.sleep(1)
    value = tempValue
    lock.release()


main()

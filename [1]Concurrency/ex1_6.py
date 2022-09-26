import time
from threading import *

val1 = 9
val2 = 4

# add lock
lock = Lock()


def main():
    global val1, val2
    t1 = Thread(target=calculate)
    t2 = Thread(target=calculate)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def calculate():
    # add global lock
    global val1, val2, lock

    # add acquire
    lock.acquire()

    delay = 0.1
    if val2 != 0:
        time.sleep(delay)
        print('Res=', int(val1 / val2), '\n')
        delay = 0.0001
    else:
        print('Cant Divide by 0')
    val2 = 0

    # add release
    lock.release()


main()

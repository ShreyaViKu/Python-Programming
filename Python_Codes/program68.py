"""
MultiThreading in python
using functions and with join
"""

from threading import Thread
from time import sleep

def Hello():
    for i in range(5):
        print("Hello ",i+1)
        sleep(0.5)

def Hi():
    for i in range(5):
        print("Hii ",i+1)
        sleep(0.5)

print(__name__)

if (__name__ == '__main__'):
    thread1 = Thread(target=Hello)
    thread2 = Thread(target=Hi)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End of code")

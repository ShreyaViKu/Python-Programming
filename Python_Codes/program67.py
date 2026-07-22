"""
MultiThreading in python
using functions and without join
"""

from threading import Thread

def Hello():
    for i in range(5):
        print("Hello ",i+1)

def Hi():
    for i in range(5):
        print("Hii ",i+1)

thread1 = Thread(target=Hello)
thread2 = Thread(target=Hi)

thread1.start()
thread2.start()


print("End of code")
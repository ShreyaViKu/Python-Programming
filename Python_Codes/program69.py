"""
Traffic signal using multithreading and sleep
"""

from threading import Thread
from time import sleep

def Red():
    sleep(0.5)
    print("Red : Stop")
    sleep(0.5)

def Yellow():
    sleep(0.3)
    print("Yellow : See")
    

def Green():
    sleep(0.6)
    print("Green : Go")
    

if(__name__ == "__main__"):

    t1 = Thread(target=Green)
    t2 = Thread(target=Yellow)
    t3 = Thread(target=Red)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("End of code")

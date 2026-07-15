"""
array creation from importing module array
searching of element
"""

from array import *

class arrayX:
    def __init__(self,size):
        self.size = size
        self.arr = array('i',[0]*size)

    def initialize(self):
        for i in range(size):
            self.arr[i] = int(input(f"Enter element at position {i+1} : "))

    def Display(self):
        for i in self.arr:
            print(i,end="  ")
        print()

    def Search(self,a):
        result = False
        for i in self.arr:
            if(i == a):
                result =  True
        return result
    
size = int(input("enter array size : "))

arr1 = arrayX(size)
arr1.initialize()
arr1.Display()

a = int(input("Enter number to be searched : "))
if arr1.Search(a):
    print("Element found")
else:
    print("Element not found")
            
            

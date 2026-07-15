"""
class array and input elements from user for array
but using list not array
and count even elements
"""
class array:

    def __init__(self,size):
        self.size = size
        self.arr = [0] * size

    def initalize(self):

        for i in range(self.size):
            self.arr[i] = int(input(f"enter number at {i}th position : "))

    def Display(self):
        for i in self.arr:
            print(i, end="  ")
        print()

    def CountEven(self):
        iCount = 0
        for i in self.arr:
            if(i % 2 == 0):
                iCount+=1
        return iCount

a = int(input("enter size : "))
a1 = array(a)
a1.initalize()
a1.Display()
print("Even elements are : ",a1.CountEven())




        
"""
Reverse all bits of number
"""

class ArrayX:
    def __init__(self, arr):
        self.arr = arr
    def Reverse(self):
        result = 0

        for i in range(32):
            result = result << 1
            result = result | (self.arr & 1)
            self.arr = self.arr >> 1
        return result


n = int(input("Enter Number : "))
aobj = ArrayX(n)
print("Reversed number is : ",aobj.Reverse())




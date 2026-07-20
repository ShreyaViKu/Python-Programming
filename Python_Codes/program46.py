"""
find missing number from 1 to N
"""

class ArrayX:
    def __init__(self,n,arr):
        self.n = n
        self.arr = arr
    def FindMissing(self):

        xor1 = 0
        xor2 = 0

        for i in range(self.n+1):
            xor1 = xor1 ^ i
        for i in self.arr:
            xor2 = xor2 ^ i

        return xor1 ^ xor2


arr = [1,3,2,4,5,6]

aobj = ArrayX(7,arr)

print("Missing element is : ",aobj.FindMissing())

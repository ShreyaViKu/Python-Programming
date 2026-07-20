"""
return the position of leftmost and rightmost on bit
"""

class ArrayX:
    def __init__(self, arr):
        self.arr = arr
    def RightMostOn(self):
        iPos = 0
        mask = 1
        for i in range(1,33):
            if(mask & self.arr != 0):
                iPos = i
                break
            mask = mask << 1
        return iPos
    def LeftMostOn(self):
        iPos = 0
        mask = 1 << 31
        for i in range(32,0,-1):
            if(mask & self.arr != 0):
                iPos = i
                break
            mask = mask >> 1
        return iPos


n = int(input("Enter Number : "))
aobj = ArrayX(n)
print("Right most on bit is on position : ",aobj.RightMostOn())
print("Left most on bit is on position : ",aobj.LeftMostOn())




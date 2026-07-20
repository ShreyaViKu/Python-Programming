"""
Brian Kernighan's Algorithm for finding the ON bits in the number
best approach
"""

class Bitwise:
    def __init__(self,n):
        self.n = n
    def CountOnBits(self):

        iCount = 0
        while(self.n != 0):
            self.n = self.n & self.n-1
            iCount+=1
        return iCount
    
n = int(input("Enter number : "))
bobj = Bitwise(n)

iRet = bobj.CountOnBits()

print("number of on bits are : ",iRet)
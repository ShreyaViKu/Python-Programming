"""
Accept number from user and 
count the number of ON and OFF bits in the number
"""

class Bitwise:
    def __init__(self,n):
        self.n = n
    def CountOnBits(self):
        mask = 0x1
        Count = 0
        for i in range(1,33):
            if((mask & self.n) == mask):
                Count+=1
            mask = mask << 1
        return Count
    
    def CountOffBits(self):
        mask = 0x1
        Count = 0
        for i in range(1,33):
            if((mask & self.n) == 0):
                Count+=1
            mask = mask << 1
        return Count
        
n = int(input("Enter number : "))

bobj = Bitwise(n)

iRet = bobj.CountOffBits()
print("Number of Off bits are : ",iRet)

iRet = bobj.CountOnBits()
print("Number of On bits are : ",iRet)

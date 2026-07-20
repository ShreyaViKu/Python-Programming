"""
Set the last N bits.
"""

class ArrayX:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def SetBits(self):
        mask = 1
        
        mask = (mask << self.n2) -1

        return mask | self.n1


n1 = int(input("Enter number : "))
n2 = int(input("Enter bit limit : "))

aobj = ArrayX(n1,n2)

print("Updated number is : ",aobj.SetBits())
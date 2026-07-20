"""
Accept number from user and 
off the bit at 23th position if its on
"""

class Bitwise:
    def __init__(self,n):
        self.n = n
    def OffBit(self):
        mask = 0x400000
        ans = (~mask) & self.n
        return ans
        
n = int(input("Enter number : "))

bobj = Bitwise(n)
bNum = bobj.OffBit()
print("Updated number is : ",bNum)

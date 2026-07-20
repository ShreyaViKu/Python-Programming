"""
Toggle the bit at ith position
"""
class Bitwise:
    def __init__(self,n):
        self.n = n
    def ToggleBit(self,iPos):
        mask = 0x1
        mask = mask << (iPos-1)

        ans = mask ^ self.n
        return ans
        
n = int(input("Enter number : "))
iPos = int(input("Enter position to toggle : "))

bobj = Bitwise(n)
bNum = bobj.ToggleBit(iPos)
print("toggled number is : ",bNum)


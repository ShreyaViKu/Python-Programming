"""
Toggle the 7th and 12th bit of number 
"""
class Bitwise:
    def __init__(self,n):
        self.n = n
    def ToggleBits(self):
        mask = 0x840
        ans = mask ^ self.n
        return ans
        
n = int(input("Enter number : "))

bobj = Bitwise(n)
bNum = bobj.ToggleBits()
print("toggled number is : ",bNum)


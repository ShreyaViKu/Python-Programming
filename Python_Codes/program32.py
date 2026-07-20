"""
Decimal to binary convesion
"""
class Bitwise:
    def __init__(self,n):
        self.n = n
    def ToBinary(self):
        bNum = []
        while(self.n != 0):
            bNum.append(self.n%2)
            self.n = self.n//2
        bNum.reverse()
        return int("".join(map(str,bNum)))
        
n = int(input("Enter number : "))

bobj = Bitwise(n)
bNum = bobj.ToBinary()
print("Binary num is : ",bNum)


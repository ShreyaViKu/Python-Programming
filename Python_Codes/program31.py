"""
checking bit on position on or of
"""
class Bitwise:
    def __init__(self,n):
        self.n = n
    def CheckOn(self,iPos):
        mask = 0x1
        mask = mask << (iPos-1)
        ans = mask & self.n

        if(mask == ans):
            return True
        else:
            return False
        
n = int(input("Enter number : "))
iPos = int(input("Enter position to chaeck : "))

if(iPos<1 or iPos>32):
    print("invalid position")
else:
    bobj = Bitwise(n)

    if(bobj.CheckOn(iPos)):
        print(iPos,"th bit is on")
    else:
        print(iPos,"th bit is off")
"""
Count capitle and small leters in string
"""
class StringX:
    def __init__(self,s):
        self.s = s
    def Display(self):
        print(" ".join(self.s))
        print()
    def CountCapital(self):
        iCount = 0
        for c in self.s:
            if((c >= 'A') & (c <= 'Z')):
                iCount+=1
        return iCount
    
    def CountSmall(self):
        iCount = 0
        for c in self.s:
            if((c >= 'a') & (c <= 'z')):
                iCount+=1
        return iCount

a =input("enter string : ")

sobj = StringX(a)
sobj.Display()
print("Capital letters are : ",sobj.CountCapital())
print("Small letters are : ",sobj.CountSmall())
print("Total letters are : ",len(a))
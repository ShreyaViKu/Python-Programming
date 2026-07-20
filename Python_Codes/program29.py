"""
O
LO
LLO
ELLO
HELLO
"""
class StringX:
    def __init__(self,s):
        self.s = s
    def Display(self):
        print(" ".join(self.s))
        print()
    def Reverse(self):
        for i in range(len(self.s)-1,-1,-1):
            print(self.s[i:])

a =input("enter string : ")

sobj = StringX(a)
sobj.Display()
sobj.Reverse()
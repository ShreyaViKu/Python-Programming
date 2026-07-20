

class StringX:
    def __init__(self,s):
        self.s = s
    def Display(self):
        for c in self.s:
            print(c,end="  ")
        print()

a =input("enter string : ")

sobj = StringX(a)
sobj.Display()

print(len(a))
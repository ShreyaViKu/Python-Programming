"""
Check whether two numbers are equal using XOR
"""

class ArrayX:
    def __init__(self, no1,no2):
        self.no1 = no1
        self.no2 = no2
    def IsEqual(self):
        if(self.no1 ^ self.no2 == 0):
            return True
        else:
            return False


n1 = int(input("Enter First Number : "))
n2 = int(input("Enter second number : "))
aobj = ArrayX(n1,n2)

if(aobj.IsEqual()):
    print("they are equal")
else:
    print("They are not equal")
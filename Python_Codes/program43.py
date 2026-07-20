"""
Reverse all bits of number
"""

class ArrayX:
    def __init__(self, no1,no2):
        self.no1 = no1
        self.no2 = no2
    def Swap(self):
        self.no1 = self.no1 ^ self.no2
        self.no2 = self.no1 ^ self.no2
        self.no1 = self.no1 ^ self.no2

        return self.no1, self.no2



n1 = int(input("Enter First Number : "))
n2 = int(input("Enter second number : "))
aobj = ArrayX(n1,n2)
no1, no2 = aobj.Swap()

print("After swapping:")
print("First Number :", no1)
print("Second Number :", no2)
"""
ip = 7
1  *  3  *  5  *  7  
"""

class pattern:

    def __init__(self,n):
        self.n = n

    def PPrinting(self):
        for i in range(1,self.n+1):
            if(i % 2 == 0):
                print("*",end="\t")
            else:
                print(i,end="\t")
        print()

n = int(input("Enter number : "))
p1 = pattern(n)

p1.PPrinting()
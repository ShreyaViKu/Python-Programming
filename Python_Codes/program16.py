"""
ip = 11
*  *  *  #  #  #  *  *  *  #  #  
"""

class pattern:

    def __init__(self,n):
        self.n = n

    def PPrinting(self):
        for i in range(1,self.n+1):
            if ((i-1 )// 3) % 2 == 0:
                print("*", end="  ")
            else:
                print("#", end="  ")
            

n = int(input("Enter character : "))
p1 = pattern(n)

p1.PPrinting()
"""
ip = g
a  *  c  *  e  *  g 
"""

class pattern:

    def __init__(self,n):
        self.n = n

    def PPrinting(self):
        for i in range(ord('a'),ord(self.n)+1):
            if((i-ord('a')) % 2 == 0):
                print(chr(i),end="\t")
            else:
                print("*",end="\t")
                
        print()

n = (input("Enter character : "))[0]
p1 = pattern(n)

p1.PPrinting()
"""
iRow = 4    iCol = 4
#  &  #  &
#  &  #  &
#  &  #  &
#  &  #  & 
"""

class pattern:

    def __init__(self,iRow, iCol):
        self.iRow = iRow
        self.iCol = iCol

    def PPrinting(self):
        for i in range(1,self.iRow+1):
            for j in range(1,self.iCol+1):
                if(j % 2 == 0):
                    print("&",end="\t")
                else:
                    print("#",end="\t")
            print()
            

n1 = int(input("Enter number of rows : "))
n2 = int(input("Enter number of columns : "))
p1 = pattern(n1,n2)

p1.PPrinting()
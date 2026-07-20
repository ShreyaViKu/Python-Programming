"""
4  4  4  4
3  3  3  3
2  2  2  2
1  1  1  1  by reversing the outer loop
"""

class Pattern:
    def __init__(self,iRow, iCol):
        self.iRow = iRow
        self.iCol = iCol

    def PPrint(self):
        for i in range(self.iRow,0,-1):
            for j in range(1,self.iCol+1):
                print(i,end="\t")
            print()

iRow = int(input("Enter number of rows : "))
iCol = int(input("Enter number of columns : "))

pobj =Pattern(iRow,iCol)

pobj.PPrint()



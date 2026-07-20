"""
*
*  *
*     *
*        *
*           *
*  *  *  *  *  *
"""

class Pattern:
    def __init__(self,iRow, iCol):
        self.iRow = iRow
        self.iCol = iCol

    def PPrint(self):
        if(self.iRow != self.iCol):
            print("Invalid input")
        else:
            for i in range(1,self.iRow+1):
                for j in range(1,i+1):
                    if(j==1 or j==self.iCol or j == i or i == self.iRow):
                        print("*",end="\t")
                    else:
                        print(" ",end="\t")
                print()
        


iRow = int(input("Enter number of rows : "))
iCol = int(input("Enter number of columns : "))

pobj =Pattern(iRow,iCol)

pobj.PPrint()



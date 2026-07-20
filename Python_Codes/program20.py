"""
$  @  @  @
@  $  @  @
@  @  $  @
@  @  @  $
with backward outer loop
"""

class Pattern:
    def __init__(self,iRow, iCol):
        self.iRow = iRow
        self.iCol = iCol

    def PPrint(self):
        if(self.iRow == self.iCol):
            for i in range(1,self.iRow+1):
                for j in range(1,self.iCol+1):
                    if(i == j):
                        print("$",end="\t")
                    else:
                        print("@",end="\t")
                print()
        else:
            print("Invalid input")


iRow = int(input("Enter number of rows : "))
iCol = int(input("Enter number of columns : "))

pobj =Pattern(iRow,iCol)

pobj.PPrint()



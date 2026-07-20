"""
%  %  %  %  %  %
%  @  @  @  @  %
%  @  @  @  @  %
%  @  @  @  @  %
%  @  @  @  @  %
%  %  %  %  %  %
"""

class Pattern:
    def __init__(self,iRow, iCol):
        self.iRow = iRow
        self.iCol = iCol

    def PPrint(self):
        for i in range(1,self.iRow+1):
            for j in range(1,self.iCol+1):
                if(i==1 or i==self.iRow or j==1 or j==self.iCol):
                    print("%",end="\t")
                else:
                    print("@",end="\t")
            print()
        


iRow = int(input("Enter number of rows : "))
iCol = int(input("Enter number of columns : "))

pobj =Pattern(iRow,iCol)

pobj.PPrint()



"""
* 
*  *  
*  *  *  
*  *  *  *   
optimized reduced loop printing
TC >O(N^2/2)
"""

class Pattern:
    def __init__(self,iRow):
        self.iRow = iRow

    def PPrint(self):
        for i in range(1,self.iRow+1):
            for j in range(1,i+1):
                print("*",end="\t")
            print()
        


iRow = int(input("Enter number of rows : "))

pobj =Pattern(iRow)

pobj.PPrint()



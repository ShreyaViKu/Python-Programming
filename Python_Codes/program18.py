"""
iRow = 4    iCol = 4
$  $  $  $
#  #  #  #
$  $  $  $
#  #  #  #

without using if else with char array
"""

class pattern:

    def __init__(self,iRow, iCol):
        self.iRow = iRow
        self.iCol = iCol

    def PPrinting(self):
        for i in range(1,self.iRow+1):
            for j in range(1,self.iCol+1):
                print(char[i % 2],end="  ")
            print()
            

# n1 = int(input("Enter number of rows : "))
# n2 = int(input("Enter number of columns : "))
n1, n2 = map(int, input("Enter row, columns: ").split(' '))

p1 = pattern(n1,n2)

p1.PPrinting()
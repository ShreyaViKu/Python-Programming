"""
find unique element from array if other element appears twice in array
"""

class ArrayX:
    def __init__(self,arr):
        self.arr = arr
    def FindSingle(self):
        result = 0

        for i in self.arr:
            result = result ^ i

        return result


arr = [1,3,4,3,2,4,5,2,1]

aobj = ArrayX(arr)

print("Unique single element is : ",aobj.FindSingle())

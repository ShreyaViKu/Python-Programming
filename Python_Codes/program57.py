"""
Addition of N numbers 
"""

def Addition(arr,index):
    if index == len(arr):
        return 0
    return arr[index] + Addition(arr,index+1)


arr = [10,20,30,40,50]


print("Addition of Numbers is : ",Addition(arr,0))


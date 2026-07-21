"""
Addition of N numbers 
with elements from user
"""

def Addition(arr,index):
    if index == len(arr):
        return 0
    return arr[index] + Addition(arr,index+1)


arr = list(map(int, input("Enter elements with space : ").split()))

print(arr)


print("Addition of Numbers is : ",Addition(arr,0))


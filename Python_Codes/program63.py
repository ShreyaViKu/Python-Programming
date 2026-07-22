"""
factirial with recursion 
highorder operator for returning list of squares of numbers
from given list
"""
def fact(num):
    if(num == 1):
        return 1
    return num * fact(num-1)

def square(nums):

    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]
    return nums

def Operate(nums, operation):
    return operation(nums)

num = int(input("enter Number : "))

arr =[]
for i in range(0,num):
    arr.append(int(input(f"enter {i}th element of list")))

result = Operate(arr,square)

print("Result list is : ",result)
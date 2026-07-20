"""
accept number from user and 
check if it is power of 2 or not 
using bitwise operations
"""

n = int(input("Enter number : "))

mask = 1
if(n == 0):
    print(n," is Power of 2")
elif(n & (n-1) == 0):
    print(n," is Power of 2")
else:
    print(n," is not a Power of 2")



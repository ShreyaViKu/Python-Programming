"""
Factorial of Number with recursion
"""

def Factorial(iNo):
    if(iNo == 1 or iNo == 0):
        return 1
    return (iNo * Factorial(iNo-1))

no = int(input("Enter Number : "))
print("Factorial of number is : ",Factorial(no))


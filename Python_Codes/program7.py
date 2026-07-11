"""
Display factors and sum of factors
"""

def Factors(a):
    sum = 0
    for i in range(2,a):
        if(a % i == 0):
            print(i,end="  ")
            sum+=i
    print("\nSum of factors is : ",sum)

a = int(input("Enter number : "))

Factors(a)
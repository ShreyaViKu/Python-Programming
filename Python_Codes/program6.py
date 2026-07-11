"""
Number divisible by 3 and 5
"""
def DivisibleBy3And5(a):
    if(a%3 == 0 & a %5==0):
        return True
    else:
        return False

a= int(input("Enter Number : "))

if(DivisibleBy3And5(a)):
    print("Divisible by 3 And 5")
else:
    print("Not Divisible by 3 And 5")

"""
Perfect number
"""

def PerfectNo(a):
    sum = 0
    
    for i in range(2,a):
        if(a % i == 0):
            sum+=i
    if(sum == a):
        return True
    else:
        return False

a = int(input("Enter number : "))

if(PerfectNo(a)):
    print("Perfect NUmber ")
else:
    print("Not a perfect Number")
"""
Check Palindrome using Recursion
"""

def Reverse(iNo,rev = 0):
    if(iNo == 0):
        return rev
    return Reverse(iNo // 10, ((rev*10) + iNo % 10)) 

def Palindrome(iNo):
    if(iNo == Reverse(iNo)):
        return True
    else:
        return False
    

no = int(input("Enter Number : "))
if(Palindrome(no)):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")


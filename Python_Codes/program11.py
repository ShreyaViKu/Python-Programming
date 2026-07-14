"""
Palindrome number
"""
def PalindromeNum(a):
    b = 0
    o = a

    while(a != 0):

        b = (10 * b)+(a % 10)
        a = a // 10

    if(b == o):
        return True
    else:
        return False
        
i = int(input("enter number : "))

if(PalindromeNum(i)):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
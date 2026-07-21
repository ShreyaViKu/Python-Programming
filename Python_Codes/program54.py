"""
digit display and sum of all digits of a number 
tail Recursive apporch
"""
# Tail recursion
def Display(iNo):
    if(iNo == 0):
        return
    print(iNo % 10)
    Display(iNo // 10)

def Summation(iNo):
    if(iNo == 0):
        return 0
    return (iNo % 10) + (Summation(iNo // 10))

no = int(input("Enter Number : "))
Display(no)
print("Summation of digits is : ",Summation(no))


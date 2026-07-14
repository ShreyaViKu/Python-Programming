"""
printing digits in the number
"""

def DisplayDigits(i):
    
    if(i<0):
        i= -i

    while(i != 0):
        a = i % 10
        print(a)
        i = (i // 10)

a = int(input("Enter number : "))

DisplayDigits(a)
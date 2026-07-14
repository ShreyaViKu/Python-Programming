"""
Even Odd digit sum and difference
"""

def EvenOddDigit(a):
    SumEven = 0
    SumOdd = 0

    while(a != 0):
        i = a % 10
        if( i % 2 == 0):
            SumEven+=i
        else:
            SumOdd+=i
        a = a // 10

    print("Even digit sum is ",SumEven)
    print("Odd digits sum is ",SumOdd)
    print("Difference between even odd digits is ",(SumEven - SumOdd))

a = int(input("Enter number : "))
EvenOddDigit(a)
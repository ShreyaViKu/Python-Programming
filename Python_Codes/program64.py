"""
Even odd lambda function with 2 approach
"""
EvenOdd1 = lambda num : num % 2 == 0

EvenOdd2 = lambda num : "Even" if num % 2 == 0 else "Odd"
num = int(input("Enter number : "))

if(EvenOdd1(num)):
    print("Even Number")
else:
    print("Odd Number")

print(EvenOdd2(num))

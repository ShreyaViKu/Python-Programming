"""
Even Odd using bitwise
as if LSB is off its even 
as no extra 1 is added
"""

n = int(input("Enter number : "))

mask = 1

if(mask & n == 0):
    print("Number is Even")
else:
    print("Number is Odd")
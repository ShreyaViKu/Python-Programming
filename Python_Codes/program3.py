def EvenOdd(a):
    if(a % 2 == 0):
        return True
    else:
        return False
    

a = int(input("Enter number : "))

if(EvenOdd(a)):
    print("Even number")
else:
    print("Odd number")

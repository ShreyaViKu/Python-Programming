"""
table in reverse and in normal order
"""
a = int(input("Enter number : "))

print("table is : ")

for i in range(1,11):
    print(a," * ",i," = ",i*a)

print("table in reverse is : ")

for i in range(10,0,-1):
    print(a," * ",i," = ",i*a)
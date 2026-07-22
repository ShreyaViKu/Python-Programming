"""
filter and lambda function for getting numbers greater than 50
map function to take input list from user 
"""

l1 = list(map(int,input("Enter Number : ").split(" ")))

l2 = list(filter(lambda n : n > 50, l1))

print(l2)
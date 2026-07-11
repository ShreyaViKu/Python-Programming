def ElectionAge(a):

    if(a<18):
        print("you are under age")
    elif(a>80):
        print("You are over aged")
    else:
        print("you can vote yeee!!")

a = int(input("Enter your age : "))

ElectionAge(a)
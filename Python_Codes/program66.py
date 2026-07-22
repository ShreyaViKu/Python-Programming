"""
inner function and outer function 
"""
def greet():

    print("Welcome to function")

    def message(name):

        print("hello ",name)

    return message

fun = greet()

fun("Shreya")
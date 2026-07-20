"""
Toggle letters in string
"""
class StringX:
    def __init__(self,s):
        self.s = s
    def Display(self):
        print(" ".join(self.s))
        print()
    def ToggleLetters(self):
        result = ""
        
        for c in self.s:
            if 'A' <= c <= 'Z':
                result += chr(ord(c) + 32)
            elif 'a' <= c <= 'z':
                result += chr(ord(c) - 32)
            else:
                result += c
        return result
        

a =input("enter string : ")

sobj = StringX(a)
sobj.Display()
print("Toggled string is : ",sobj.ToggleLetters())
print("Total letters are : ",len(a))
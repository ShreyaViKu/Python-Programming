"""
Stack code
"""

class node:
    def __init__(self,iNo):
        self.data = iNo
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.iCount = 0
    def Display(self):
        temp = self.first
        while(temp != None):
            print("| ",temp.data," |")
            temp = temp.next
        print()
    def push(self,iNo):
        newn = node(iNo)

        if(self.first == None):
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn
        self.iCount+=1
    def pop(self):
        if(self.first == None):
            print("stack is empty")
            return 
        
        temp = self.first
        self.first = self.first.next
        self.iCount -= 1

        return temp.data
    def peek(self):
        if(self.first == None):
            print("stack is empty")
            return 
        else:
            return self.first.data
    def Count(self):
        return self.iCount

            

sobj = Stack()

sobj.push(51)
sobj.push(21)
sobj.push(11)

sobj.Display()
print("Number of elements are : ",sobj.Count())

print("Popped element is : ",sobj.pop())

sobj.Display()
print("Number of elements are : ",sobj.Count())

print("peeped element is : ", sobj.peek())

sobj.Display()
print("Number of elements are : ",sobj.Count())


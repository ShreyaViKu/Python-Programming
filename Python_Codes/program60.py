"""
Queue code
"""

class node:
    def __init__(self,iNo):
        self.data = iNo
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def Display(self):
        temp = self.first
        while(temp != None):
            print("| ",temp.data," |")
            temp = temp.next
        print()

    def Enqueue(self,iNo):
        newn = node(iNo)

        if(self.first == None):
            self.first = newn
        else:
            temp = self.first
            while(temp.next != None):
                temp = temp.next
            temp.next = newn
        
        self.iCount+=1

    def Dequeue(self):
        if(self.first == None):
            print("Queue is empty")
            return 
        
        temp = self.first
        self.first = self.first.next
        self.iCount -= 1

        return temp.data
    
    def Count(self):
        return self.iCount

            

sobj = Queue()

sobj.Enqueue(11)
sobj.Enqueue(21)
sobj.Enqueue(51)
sobj.Enqueue(101)

sobj.Display()
print("Number of elements are : ",sobj.Count())

print("Removed element is : ",sobj.Dequeue())

sobj.Display()
print("Number of elements are : ",sobj.Count())

"""
Queue reverse Display
Minimum and Maximum element
"""

class node:
    def __init__(self,iNo):
        self.data = iNo
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def Display(self,temp):

        if(temp == None):
            return
        print("| ",temp.data," |")
        self.Display(temp.next)
    
    def DisplayReverse(self,temp):

        if(temp == None):
            return
        self.DisplayReverse(temp.next)
        print("| ",temp.data," |")

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
    
    def Min(self):
        temp = self.first
        min = self.first.data
        while(temp != None):
            if(temp.data < min):
                min = temp.data
            temp = temp.next
        return min
    
    def Max(self):
        temp = self.first
        max = self.first.data
        while(temp != None):
            if(temp.data > max):
                max = temp.data
            temp = temp.next
        return max

            

sobj = Queue()

sobj.Enqueue(11)
sobj.Enqueue(21)
sobj.Enqueue(51)
sobj.Enqueue(101)

sobj.Display(sobj.first)
print("Number of elements are : ",sobj.Count())

sobj.DisplayReverse(sobj.first)

print("minimum element of Queue is : ",sobj.Min())

print("maximum element of Queue is : ",sobj.Max())

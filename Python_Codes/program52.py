"""
Doubly Circular Linked List
All functions
"""

class node:
    def __init__(self,iNo):
        self.data = iNo
        self.next = None
        self.prev = None

class DoublyCL:
    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0

    def Display(self):
        temp = self.first
        print("-> ",end=" ")
        while True:
            print("| ",temp.data," | -> ",end=" ")
            temp = temp.next
            if(temp == self.first):
                break
        print()
    
    def Count(self):
        return self.iCount
    
    def InsertFirst(self,iNo):
        newn = node(iNo)

        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.last.next = self.first
        self.first.prev = self.last
        self.iCount+=1

    def InsertLast(self,iNo):
        newn = node(iNo)

        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
        else:
            self.last.next = newn
            newn.prev = self.last
            self.last = newn

        self.last.next = self.first
        self.first.prev = self.last
        self.iCount+=1

    def InsertAtPos(self,iNo,iPos):
        if((iPos < 1) | (iPos > self.iCount+1)):
            print("Invalid Position")
            return 
        if(iPos == 1):
            self.InsertFirst(iNo)
        elif(iPos == self.iCount+1):
            self.InsertLast(iNo)
        else:
            temp = self.first
            for i in range(1,iPos-1):
                temp = temp.next
            newn = node(iNo)
            newn.next = temp.next
            temp.next.prev = newn
            newn.prev = temp
            temp.next = newn

            self.iCount+=1

    def DeleteFirst(self):
        if(self.first == None and self.last == None):
            return
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            self.first.prev = self.last
            self.last.next = self.first

        self.iCount-=1

    def DeleteLast(self):
        if(self.first == None and self.last == None):
            return
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            self.last = self.last.prev
            self.first.prev = self.last
            self.last.next = self.first
            
        self.iCount-=1
    
    def DeleteAtPos(self,iPos):
        if((iPos < 1) | (iPos > self.iCount)):
            print("Invalid Position")
            return 
        if(iPos == 1):
            self.DeleteFirst()
        elif(iPos == self.iCount):
            self.DeleteLast()
        else:
            temp = self.first
            for i in range(1,iPos-1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp

            self.iCount-=1


sobj = DoublyCL()

sobj.InsertFirst(51)
sobj.InsertFirst(21)
sobj.InsertFirst(11)

sobj.Display()
print("Number of elements are : ",sobj.Count())

sobj.InsertLast(101)
sobj.InsertLast(111)
sobj.InsertLast(121)

sobj.Display()
print("Number of elements are : ",sobj.Count())

sobj.InsertAtPos(105,4)

sobj.Display()
print("Number of elements are : ",sobj.Count())

sobj.DeleteAtPos(4)

sobj.Display()
print("Number of elements are : ",sobj.Count())

sobj.DeleteFirst()
sobj.DeleteLast()

sobj.Display()
print("Number of elements are : ",sobj.Count())



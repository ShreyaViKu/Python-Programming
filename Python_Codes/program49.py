"""
Singly Linear Linked List
All functions
"""

class node:
    def __init__(self,iNo):
        self.data = iNo
        self.next = None

class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def Display(self):
        temp = self.first
        while(temp != None):
            print("| ",temp.data," | -> ",end=" ")
            temp = temp.next
        print("None")
    
    def Count(self):
        return self.iCount

    def InsertFirst(self,iNo):
        newn = node(iNo)

        if(self.first == None):
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn
        self.iCount+=1
    
    def InsertLast(self,iNo):
        newn = node(iNo)

        if(self.first == None):
            self.first = newn
        else:
            temp = self.first

            while(temp.next != None):
                temp = temp.next
            temp.next = newn
        self.iCount+=1

    def InsertAtPos(self,iNo,iPos):
        if((iPos < 1) | (iPos > self.iCount+1)):
            print("Invalid position")
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
            temp.next = newn

            self.iCount+=1
    
    def DeleteFirst(self):
        if(self.first == None):
            return
        else:
            self.first = self.first.next
        self.iCount-=1

    def DeleteLast(self):
        if(self.first == None):
            return
        elif(self.first.next == None):
            self.first = None
        else:
            temp = self.first
            while(temp.next.next != None):
                temp = temp.next
            temp.next = None
        self.iCount-=1

    def DeleteAtPos(self,iPos):
        if((iPos < 1 )|(iPos > self.iCount)):
            print("Invalid position")
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

            self.iCount-=1
        

sobj = SinglyLL()

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

sobj.DeleteFirst()

sobj.Display()
print("Number of elements are : ",sobj.Count())

sobj.DeleteLast()

sobj.Display()
print("Number of elements are : ",sobj.Count())

sobj.DeleteAtPos(3)

sobj.Display()
print("Number of elements are : ",sobj.Count())
        
"""
Singly Linear Linked List
Insert and Display
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



        
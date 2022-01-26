class Node:
    def __init__(self,value):
        self.next=None
        self.value=value

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def prepend(self,value):
        new_node=Node(value)
        temp=self.head
        self.head=new_node
        self.head.next=temp
        del temp
        self.length+=1

    def insert(self,value,index):
        new_node=Node(value)
        count=1
        temp=self.head
        while count != index:
            temp=temp.next
            count+=1
        c=temp
        temp=temp.next
        c.next=new_node
        new_node.next=temp
        self.length+=1

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

mylist=LinkedList(78)
mylist.append(24)
mylist.append(56)
mylist.append(53)
mylist.printlist()
print(mylist.length)
mylist.insert(78,4)
print(mylist.length)
mylist.printlist()

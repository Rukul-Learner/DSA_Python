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
        return True

    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    # def insert(self,value,index):
    #     new_node=Node(value)
    #     count=1
    #     temp=self.head
    #     while count != index:
    #         temp=temp.next
    #         count+=1
    #     c=temp
    #     temp=temp.next
    #     c.next=new_node
    #     new_node.next=temp
    #     self.length+=1

    def insert(self,index,value):
        if index<0 or index>self.length:
            return None
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        temp=self.get(index-1)
        new_node.next=temp.next
        temp.next=new_node
        self.length+=1
        return True

    def pop(self,index=-1):
        if self.length==0:
            return None
        temp = pre = self.head
        while(temp.next):
            pre =temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp

    def set_v(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

mylist=LinkedList(2)
mylist.append(3)
mylist.prepend(1)
mylist.printlist()

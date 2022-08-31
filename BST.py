# Node Constructor
class Node:
    def __init__(self, value):
        self.value=value
        self.right=None
        self.left=None

#BST Constructor
class BinarySearchTree:
    # def __init__(self,value):
    #    new_node = Node(value)
    #    self.root = new_node

    # Empty BST Constructor
    def __init__(self):
        self.root = None

    # Node Insertion Method
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            if new_node.value>temp.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
            else:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left

    # Method to check if BST contains a Node value
    def contains(self, value):
        if self.root is None:
            return False
        temp=self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value > temp.value:
                temp=temp.right
            else:
                return True
        return False

    # Method to find Minimum value node in BST or it's subtree
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node=current_node.left
        return current_node

    # Method to find Maximum value node in BST or it's subtree
    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

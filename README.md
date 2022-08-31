These are my practice codes for DSA using Python.

Linked Lists:
A linked list is a data structure containing nodes, where each node points to next node and the last node points to None.
It does not have indexing and the nodes are not present in contiguous memory locations.
Have a variable "Head" pointing to the first node and "Tail" pointing to the last node in the list.

Doubly Linked List:
A doubly linked list is an extension of a Linked List. In a doubly linked list each node points to the next node and the previous node.

Circularly Linked List:
A circular linked list is a type of linked list in which the first and the last nodes are also connected to each other to form a circle. The address of the last node consists of the address of the first node.

Circularly Doubly Linked List:
A circular doubly linked list is a type of doubly linked list in which the first and the last nodes are also connected to each other to form a circle. The address of the last node consists of the address of the first node.

Stacks:
Stack is a LIFO data structure i.e Last-In First-Out. Stacks are usually implemented with arrays/lists. An item is pushed at top of stack. The last item pushed is the first item to be popped out of the stack.
Here, I have used linked lists to implement stack.

Queue:
Queue is a FIFO data structure i.e First-In First-Out. Queues are usually implemented with lists/arrays. An item is enqueued at last of a queue. An item is dequeued from the beginning of a queue. Peek function is used to return the value of first item without dequeuing it.
Here, I have used linked lists to implement queue.

Trees:
A tree is a non-linear data structure as it does not store nodes in a sequential manner.
It is a hierarchical data structure as nodes in a tree are arranged in multiple levels. The topmost level contains a single node termed as root node. Each node contains some data and pointers to other nodes termed as children to this node (parent node). A node with no children is called as a leaf node. Nodes that are children of same parent node are termed as sibling nodes.

Types of Trees:

1) General Trees: There is no restriction on the number of children nodes a parent node can have.  

2) Binary Trees: A node of a binary tree can have a maximum number of 2 child nodes.

3) Balanced Trees: Height of left and right subtree of any node differs by not more than 1.

4) Full Tree: Every node points to either 2 nodes or 0 nodes.

5) Perfect Tree: Any level in a tree that has any nodes is completely filled all the way across.

6) Complete Tree: The tree is filled from left to right with no gaps.

Binary Search Tree:
All the nodes to the right of a node have values greater than the value of the node and all the nodes to the left have values less than the value of the node. They can not have duplicate values.
Each node can have at-most 2 children as it is a binary tree.
In a complete, full and perfect BST, no of nodes = 2**n -1, where n = no. of levels.
They are a prime example of Divide and Conquer as their Time Complexity is O(log(n)(base2)).
In worst case scenario, a BST never forks and is straight line, therefore worst case time complexity is O(n).

Hash Tables:

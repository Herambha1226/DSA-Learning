# ------------ Singly linked list example program -------------#

# creating class of node for linkedlist 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def traversal(head): # traversal means printing all elements in list
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end=" ")
        head = head.next
    print()
    
def insert_node_head(head,x):
    newnode = Node(x)
    newnode.next = head
    return newnode

def insert_node_end(head,x):
    new_node = Node(x) 

    if head is None:
        return new_node
    
    last = head

    while last.next is not None:
        last = last.next
    
    last.next = new_node

    return head

def insert_value(pos,x,head):
    if head is None:
        return Node(x)
    elif pos < 1:
        return head
    
    if pos == 1:
        new_node = Node(x)
        new_node.next = head
        return new_node
    
    curr = head
    for i in range(1,pos - 1):
        if curr is None:
            return head
        curr = curr.next
    
    if curr is None:
        return head
    
    new_node = Node(x)

    new_node.next = curr.next
    curr.next = new_node
    return head
    
    
# create node
node1 = Node(1)
node2 = Node(3)
node3 = Node(6)
node4 = Node(4)
node5 = Node(2)

# link nodes 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

print("Before Insertion : ")
traversal(head)
head = insert_node_head(head,10)
print("After insertion : ")
traversal(head)

print("After Insertion End : ")
insert_node_end(head,20)
traversal(head)
print("After insertion in specific :")
head = insert_value(3,5,head)
traversal(head)
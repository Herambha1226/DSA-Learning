# ---------------- adding deleting operation in linked list --------------------#

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


def traversal(head):
    while head is not None:
        print(head.data,end=" ")
        if head.next is not None:
            print(" -> ",end=" ")
        head = head.next
    print()

def insert_head(head,x):
    new_node = Node(x)
    new_node.next = head
    return new_node

def insert_end(head,x):
    new_node = Node(x)

    if head is None:
        return x
    
    while head is not None:
        head = head.next
    head.next = new_node

    return head

def insert_spec_pos(pos,x,head):
    new_node = Node(x)
    if head is None:
        return new_node
    elif pos < 1:
        return head
    
    if pos == 1:
        new_node.next = head
        return head
    
    curr = head
    for i in range(1,pos - 1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head
    
    new_node.next = curr.next
    curr.next = new_node
    return head


def deleteHead(head):
    if head is None:
        return None
    
    temp = head

    head = head.next
    
    temp = None
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

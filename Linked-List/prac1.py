# Linked List Practice

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self,head):
        self.head = head
    
    def insert_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_ending(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def delete_beginning(self):
        if self.head:
            self.head = self.head.next
    
    def search(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                print(f"{data} Found !")
            temp = temp.next
        return
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->",flush=True)
            temp = temp.next
        print("Null")
    
    def insert_at_position(self,data,position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        count = 1

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1
        
        if temp is None:
            print("Position Is Out Of Range !")
        
        new_node.next = temp.next
        temp.next = new_node

    def cound_list(self):
        temp = self.head
        count = 0
        while temp:
            if temp is not None:
                temp = temp.next
                count += 1
        # print(f"Length Of LinkedList : {count}")
        return count
    
    def find_middle_ele(self):
        length = self.cound_list()
        position = (length//2)+1
        temp = self.head
        count = 1
        while count < position:
            temp = temp.next
            count += 1
        print(f"Midddle Element : {temp} Position : {count}")



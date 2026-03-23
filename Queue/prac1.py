# Queue Data Structure Problem practice

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty !"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty !"
        return self.queue[0]
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.queue)
    
    def all_Elements(self):
        return self.queue
    
    def sort(self):
        self.queue.sort() 
        return self.queue
    
    def search(self,element):
        for i in self.queue:
            if element == i:
                return "Element Found !"
        return "Element Not Found !"
    
    def reverse(self):
        temp = []
        i = len(self.queue)
        print(self.queue[i-1])
        for j in self.queue:
            temp.append(self.queue[i-1])
            i-=1
        self.queue = temp
        return temp


if __name__ == "__main__":
    Q = Queue()
    Q.enqueue(2)
    Q.enqueue(4)
    Q.enqueue(3)
    Q.enqueue(8)
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    print(" All Stored Elements: ",Q.all_Elements())
    Q.dequeue()
    Q.dequeue()
    print(" After Two Time Dequeue Poccess: ",Q.all_Elements())
    print(" Length Of the Queue: ",Q.size())
    print(" Queue is Empty or Not : ",Q.isEmpty())
    print(" Peek Element :",Q.peek())
    print(" Sorting After Elements: ",Q.sort())
    print(" Search 5 Number value is stored or not : ",Q.search(5))
    print(" Reverse Of Queue : ",Q.reverse())
    print(" Remaining All Element : ",Q.all_Elements())




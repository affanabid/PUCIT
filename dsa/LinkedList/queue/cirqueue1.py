class QueueNode:
    def __init__(self, val) -> None:
        self.info = val
        self.next = None

class CircularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def length(self):
        if self.front == -1:
            return 0
        current = self.front
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def is_empty(self):
        if self.length() == 0:
            return True
        return False

    def enqueue(self, data):
        newNode = QueueNode(data)
        if self.length() == self.size:
            return 'Size full'
        if self.is_empty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.is_empty():
            return 'Queue underflow'
        data = self.front.info
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
    
    def display(self):
        if self.front == -1 or self.front is None:
            return 
        current = self.front
        print(current.info, end=' ')
        current = current.next
        while current != self.front and current is not None:
            print(current.info, end=' ')
            current = current.next
        print()

# q = CircularQueue(5)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)

# q.display()

# q.dequeue()
# q.dequeue()

# q.display()

# q.enqueue(6)

# q.display()

if __name__ == "__main__":
    ob = CircularQueue(5)
    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)
    ob.display()
    print("Deleted value = ", ob.dequeue())
    print("Deleted value = ", ob.dequeue())
    ob.display()
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    ob.display()

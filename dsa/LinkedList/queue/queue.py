class QueueNode:
    def __init__(self, val) -> None:
        self.info = val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front is None:
            return True
        return False
    
    def enqueue(self, val):
        newNode = QueueNode(val)
        if self.is_empty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    
    def dequeue(self):
        if self.is_empty():
            return 'Queue Underflow'
        data = self.front.info
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        current = self.front
        if self.is_empty():
            print('Empty queue')
            return
        while current is not None:
            print(current.info, end=' ')
            current = current.next 
        print()

queue = Queue()

queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)

queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.display()
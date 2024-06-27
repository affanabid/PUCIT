class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
        
    def enQueue(self, data):
        newNode = Queue(data)
        if self.length() == self.size:
            return 'Size full'
        if self.is_empty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def deQueue(self):
        if self.is_empty():
            return 'Queue underflow'
        data = self.front.info
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
    
    def isEmpty(self):
        if self.length() == 0:
            return True
        return False
    
    def length(self):
        if self.front == -1:
            return 0
        current = self.front
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def isFull(self):
        if self.length() == self.size:
            return True
        return False

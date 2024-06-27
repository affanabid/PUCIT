class ListCircularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print('Queue Full')

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print('Queue Empty')
            return
        elif self.rear == self.front:
            temp = self.queue[self.front]
            self.rear = -1
            self.front = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def isempty(self):
        return self.count == 0

    def display(self):
        if self.front == -1:
            print('Queue empty')
            return 
        elif self.rear >= self.front:
            print('Elements: ', end='')
            for i in range(self.front, self.rear+1):
                print(self.queue[i], end=' ')
            print()
        else:
            print('Elements: ', end='')
            for i in range(self.front, self.size):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=' ')
            print()
        
        if (self.rear + 1) % self.size == self.front:
            print('Queue full')

cq = ListCircularQueue(5)
cq.enqueue(5)
cq.enqueue(4)
cq.enqueue(3)
cq.enqueue(2)
cq.enqueue(1)
cq.display()
cq.dequeue()
cq.dequeue()
cq.display()

# print(cq.sized())
# cq.display()
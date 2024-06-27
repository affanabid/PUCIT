class ListBaseCircularQueue:
    def __init__(self, size):
        self.size = size
        self.head = self.tail = 0
        self.count = 0
        self.queue = [] * size

    def enqueue(self, data):
        if self.count == self.size:
            raise IndexError("CircularQueue is full")
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if not self.queue or self.count == 0:
            raise IndexError("CircularQueue is empty")
        dequeued_data = self.queue[0]
        self.queue=self.queue[1:]
        self.count -= 1
        return dequeued_data
    
    def isempty(self):
        return self.count == 0

    def sized(self):
        return self.count

    def display(self):
        if not self.queue or self.count == 0:
            print("CircularQueue is empty")
            return
        for i in range(len(self.queue)):
            if self.queue[i] is not None:
                print(self.queue[i],end=' ')
        print()

    def get_item_at_index(self, index):
        if index < 0 or index >= self.sized() :
            return 'Index out of range'
        else:
            return self.queue[index]
        # if index < 0 or index >= self.count:
        #     raise IndexError("Index out of range")
        # return self.queue[(self.head + index) % self.size]
    def remove_at_index(self, index):
        del self.queue[index]

cq = ListBaseCircularQueue(5)
cq.enqueue(5)
cq.enqueue(4)
cq.enqueue(3)
cq.enqueue(2)
cq.enqueue(1)
# cq.display()
cq.remove_at_index(1)
# cq.display()

# cq.dequeue()
# cq.dequeue()
# print(cq.sized())
# cq.display()
# print(cq.get_item_at_index(5))
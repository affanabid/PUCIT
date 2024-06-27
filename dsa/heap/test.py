class Node:
    def __init__(self, letter, occ) -> None:
        self.letter = letter
        self.occ = occ

class LetterHeap:
    def __init__(self) -> None:
        self.h = []
        self.size = 0

    def insert(self, data):
        if self.size == 0:
            self.h.append(data)
            self.size += 1
            return
        self.h.append(data)
        i = self.size
        self.size += 1
        while i != 0 and self.h[(i-1)//2].occ < self.h[i].occ:
            self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
            i = (i-1) // 2

    def extractMax(self):
        if self.size == 0:
            return False
        if self.size == 1:
            self.size -= 1
            return self.h.pop()
        self.size -= 1
        popped = self.h.pop()
        mx = self.h[0]
        self.h[0] = popped

        self.heapify(0)

        return mx
    
    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        if left < self.size and self.h[left].occ > self.h[i].occ:
            largest = left
        if right < self.size and self.h[right].occ > self.h[largest].occ:
            largest = right
        if i != largest:
            self.h[i], self.h[largest] = self.h[largest], self.h[i]
            self.heapify(largest)

class maxHeap:
    def __init__(self) -> None:
        self.h = []
        self.size = 0

    def insert(self, value):
        if self.size == 0:
            self.h.append(value)
            self.size += 1
            return
        self.h.append(value)
        i = self.size
        self.size += 1
        while i != 0 and self.h[(i-1)//2] < self.h[i]:
            self.h[i], self.h[(i-1)//2] = self.h[(i-1)//2], self.h[i]
            i = (i-1) // 2

    def extractMax(self):
        if self.size == 0:
            return
        if self.size == 1:
            return self.h.pop()
        self.size -= 1
        popped = self.h.pop()
        mx = self.h[0]
        self.h[0] = popped

        self.heapify(0)

        return mx
    
    def heapify(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        if left < self.size and self.h[left] > self.h[i]:
            largest = left
        if right < self.size and self.h[right] > self.h[largest]:
            largest = right
        if i != largest:
            self.h[i], self.h[largest] = self.h[largest], self.h[i]
            self.heapify(largest)

class minHeap:
    def __init__(self) -> None:
        self.h = []
        self.size = 0

    def insert(self, value):
        if self.size == 0:
            self.h.append(value)
            self.size += 1
            return
        i = self.size
        self.size += 1
        self.h.append(value)
        while i != 0 and self.h[(i-1)//2] > self.h[i]:
            self.h[(i-1)//2], self.h[i] = self.h[i], self.h[(i-1)//2]
            i = (i-1) // 2
        
    def heapify(self, i):
        left = i // 2 + 1
        right = i // 2 + 2
        smallest = i
        if left < self.size and self.h[left] < self.h[i]:
            smallest = left
        if right < self.size and self.h[right] < self.h[smallest]:
            smallest = right
        if smallest != i:
            self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
            self.heapify(smallest)

    def extractMin(self):
        if self.size == 0:
            return
        if self.size == 1:
            return self.h.pop()
        self.size -= 1
        popped = self.h.pop()
        mn = self.h[0]
        self.h[0] = popped
        self.heapify(0)
        return mn

def max_heap_implementation():
    h = maxHeap()
    h.insert(5)
    h.insert(1)
    h.insert(10)
    h.insert(7)
    h.insert(50)

    print(h.h)

    print(h.extractMax())
    print(h.extractMax())
    print(h.extractMax())


    print(h.h)

def min_heap_implementation():
    h = minHeap()
    h.insert(5)
    h.insert(2)
    h.insert(1)
    h.insert(4)
    h.insert(3)


    print(h.h)
    
    print(h.extractMin())
    print(h.extractMin())
    print(h.extractMin())


    print(h.h)
from collections import Counter
def solution():
    h = LetterHeap()
    word = 'aabb'
    data_dict = Counter(word).items()
    for data in data_dict:
        node = Node(data[0], data[1])
        h.insert(node) 
    
    result  = ''
    while True:
        max_node = h.extractMax()
        if max_node == False:
            break
        letter = max_node.letter
        occ = max_node.occ
        curr =  letter * occ
        print(curr)
        result += curr
    print(result)

solution()


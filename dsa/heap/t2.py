class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapifyUp(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("extract_max from an empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyUp(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapifyUp(parent_index)

    def heapifyDown(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapifyDown(largest)

def max_product(nums):
    heap = MaxHeap()
    for num in nums:
        heap.insert(num)

    first_max = heap.extract_max()
    second_max = heap.extract_max()
    
    return (first_max - 1) * (second_max - 1)

print(max_product([3, 4, 5, 2]))  
print(max_product([1, 5, 4, 5]))  
print(max_product([3, 7]))        

class Student:
    def __init__(self, rollNo, cgpa):
        self.rollNo = rollNo
        self.cgpa = cgpa

class StudentMaxHeap:
    def __init__(self, size):
        self.maxSize = size
        self.currSize = 0
        self.students = [None] * size

    def isEmpty(self):
        return self.currSize == 0

    def isFull(self):
        return self.currSize == self.maxSize

    def insert(self, student):
        if self.isFull():
            return False
        self.students[self.currSize] = student
        self.heapifyUp(self.currSize)
        self.currSize += 1
        return True

    def removeBestStudent(self):
        if self.isEmpty():
            return None
        best_student = self.students[0]
        self.students[0] = self.students[self.currSize - 1]
        self.students[self.currSize - 1] = None
        self.currSize -= 1
        self.heapifyDown(0)
        return best_student

    def levelOrder(self):
        for i in range(self.currSize):
            student = self.students[i]
            print(f"Roll No: {student.rollNo}, CGPA: {student.cgpa}")

    def height(self):
        if self.currSize == 0:
            return 0
        h = (self.currSize - 1).bit_length()
        return h

    def heapifyUp(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.students[index].cgpa > self.students[parent_index].cgpa:
            self.students[index], self.students[parent_index] = self.students[parent_index], self.students[index]
            self.heapifyUp(parent_index)

    def heapifyDown(self, index):
        largest = index 
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < self.currSize and self.students[left_child_index].cgpa > self.students[largest].cgpa:
            largest = left_child_index

        if right_child_index < self.currSize and self.students[right_child_index].cgpa > self.students[largest].cgpa:
            largest = right_child_index

        if largest != index:
            self.students[index], self.students[largest] = self.students[largest], self.students[index]
            self.heapifyDown(largest)

heap = StudentMaxHeap(10)
heap.insert(Student(1, 3.8))
heap.insert(Student(2, 3.9))
heap.insert(Student(3, 3.7))
heap.insert(Student(4, 4.0))

print("Level order traversal of the heap:")
heap.levelOrder()

s = heap.removeBestStudent()
print(f"Removed Student - Roll No: {s.rollNo}, CGPA: {s.cgpa}")

s = heap.removeBestStudent()
print(f"Removed Student - Roll No: {s.rollNo}, CGPA: {s.cgpa}")

print("Level order traversal of the heap after removals:")
heap.levelOrder()

print(f"Height of the heap: {heap.height()}")

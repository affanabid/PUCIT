class Node:
    def __init__(self, val) -> None:
        self.info = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self, val):
        newNode = Node(val)
        temp = self.head
        self.head = newNode
        self.head.next = temp

    def insert_at_tail(self, val):
        newNode = Node(val)
        current = self.head
        if current is None:
            self.head = newNode
            return 
        while current.next is not None:
            current = current.next
        current.next = newNode
        # newNode.next = None

    def insert_before(self, key, val):
        newNode = Node(val)
        prev = self.head
        current = self.head
        if self.head is None:
            self.head = newNode
        while current is not None:
            if current.info == key:
                prev.next = newNode
                newNode.next = current
                return
            prev = current
            current = current.next
  
    def insert_after(self, key, val):
        newNode = Node(val)
        current = self.head
        if current is None:
            self.head = newNode
            return
        while current is not None:
            if current.info == key:
                temp = current.next
                current.next = newNode
                newNode.next = temp
                return 
            current = current.next

    def update(self, key, val):
        current = self.head
        while current is not None:
            if current.info == key:
                current.info = val
            current = current.next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.info == key:
                print('Found')
                return True
            current = current.next
        print('Not Found')
        return False

    def remove(self, key):
        prev = self.head
        current = self.head
        while current is not None:
            if current.info == key:
                prev.next = current.next
            prev = current
            current = current.next

    def combine(self, list1, list2):
        if list1.head is None:
            self.head = list2.head
            return
        if list2.head is None:
            return
        self.head = list1.head
        current = list1.head
        while current.next is not None:
            current = current.next
        current.next = list2.head
        
    # def shuffleMerge(self, list1, list2):
    #     if list1.head is None or list2.head is None:
    #         return
    #     current1 = list1.head  
    #     current2 = list2.head
    #     while current1 is not None and current2 is not None:
    #         temp1 = current1.next
    #         temp2 = current2.next

    #         current1.next = current2
    #         current2.next = temp1

    #         # current1 = current1.next
    #         current1 = temp1
    #         # current2 = current2.next
    #         current2 = temp2
    #     self.head = list1.head
    #     list1.head = None
    #     list2.head = None
    def shuffleMerge(self, list1, list2):
        # Check if both input lists are empty
        if list1.head is None or list2.head is None:
            return
        
        # Traverse both lists simultaneously and update the pointers
        current1 = list1.head
        current2 = list2.head
        while current1 is not None and current2 is not None:
            temp1 = current1.next
            temp2 = current2.next

            current1.next = current2
            current2.next = temp1

            current1 = temp1
            current2 = temp2

        # Update the head of the calling object's list
        self.head = list1.head
        # Empty the input lists
        list1.head = None
        list2.head = None

    def reverse(self):
        prev = self.head
        current = self.head.next
        prev.next = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def recursive_reverse(self):
        current = self.head
        helper_recursive(self, current)

    def removeDuplicates(self):
        prev = self.head
        current = self.head
        seen = []
        while current is not None:
            if current.info in seen:
                prev.next = current.next
            else:
                seen.append(current.info)
            prev = current
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end=' ')
            current = current.next
        print()
      
def helper_recursive(obj, current, prev=None):
    if current.next is None:
        obj.head = current
        current.next = prev
        return
    helper_recursive(obj, current.next, current)
    current.next = prev
    
    
def main():
    a = SinglyLinkedList()
    a.insert_at_head(5)
    a.insert_at_head(3)
    a.insert_at_tail(4)
    a.insert_before(5, 6)
    a.insert_after(5, 8)
    a.update(3,9)
    a.update(4,7)
    # a.search(9)
    a.remove(5)
    a.display()
    a.reverse()
    a.display()
    # a.test()
    print()
    b = SinglyLinkedList()
    b.insert_at_head(5)
    b.insert_at_head(3)
    b.insert_at_tail(4)
    b.insert_at_tail(2)
    # b.insert_at_tail(2)
    # b.insert_at_tail(3)
    b.display()
    b.recursive_reverse()
    b.display()
    c = SinglyLinkedList()
    # c.combine(a, b)
    # c.display()
    # b.removeDuplicates()
    # b.display()
    d = SinglyLinkedList()
    # d.shuffleMerge(a,b)
    # d.display()

main()
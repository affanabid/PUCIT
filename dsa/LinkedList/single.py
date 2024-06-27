class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def display(self):
        if self.head is None:
            print('Empty List')
        current = self.head
        while current is not None:
            print(current.val, end=' ')
            current = current.next
        print()

    def insert_at_head(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def insert_at_tail(self, val):
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode

    def insert_before(self, val, key):
        if self.head is None:
            return 'Empty List'
        current = self.head
        if current.val == key:
            newNode = ListNode(val)
            newNode.next = current
            self.head = newNode
            return
        while current.next is not None:
            if current.next.val == key:
                newNode = ListNode(val)
                temp = current.next
                current.next = newNode
                newNode.next = temp
                return
            current = current.next
        
    def insert_after(self, val, key):
        if self.head is None:
            return 'Empty List'
        current = self.head
        while current is not None:
            if current.val == key:
                newNode = ListNode(val)
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next

    def update(self, val, key):
        current = self.head
        while current is not None:
            if current.val == key:
                current.val = val
                return
            current = current.next

    def remove_at_head(self):
        if self.head is None:
            return 'Empty List'
        current = self.head
        self.head = current.next
        del current

    def remove_at_tail(self):
        if self.head is None:
            return 'Empty List'
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        tail = current.next
        current.next = None
        del tail

    def remove_before(self,  key):
        if self.head is None:
            return 'Empty List'
        if self.head.val == key:
            return 'First value'
        current1 = self.head
        current2 = current1.next
        if current2.val == key:
            self.head = current2
            del current1
            return
        while current2.next is not None:
            if current2.next.val == key:
                current1.next = current2.next
                del current2
                return
            current1 = current1.next
            current2 = current2.next

    def remove_after(self, key):
        if self.head is None:
            return 'Empty List'
        current1 = self.head
        current2 = current1.next
        while current2 is not None:
            if current1.val == key:
                current1.next = current2.next
                del current2
                return
            current1 = current1.next
            current2 = current2.next

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head
        current1 = None
        current2 = self.head
        while current2 is not None:
            temp = current2.next
            current2.next = current1
            current1 = current2
            current2 = temp
        self.head = current1

    def middle(self):
        current1 = self.head
        current2 = self.head
        while current2.next is not None and current2.next.next is not None:
            current1 = current1.next
            current2 = current2.next.next
        print(current1.val)

    def merge(self, list1, list2):
        current1 = list1.head
        while current1.next is not None:
            current1 = current1.next
        current2 = list2.head
        current1.next = current2

def merge(list1, list2):
    result = SinglyLinkedList()
    result.head = list1.head
    current1 = list1.head
    current2 = list2.head
    while current1.next is not None:
        current1 = current1.next
    current1.next = current2
    result.display()
s = SinglyLinkedList()
s.insert_at_head(1)
s.insert_at_tail(5)
s.insert_before(0,1)
s.insert_after(2, 5)
s.insert_at_tail(4)

s.display()

s2 = SinglyLinkedList()
s2.insert_at_head(5)
s2.insert_at_head(1)
s2.insert_at_head(7)
s2.insert_at_head(8)

s2.display()

# s.merge(s, s2)
merge(s, s2)
# s.display()
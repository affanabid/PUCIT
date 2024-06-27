class Node:
    def __init__(self, value) -> None:
        self.info = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_head(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
    
    def insert_at_tail(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
        newNode.prev = current
        self.tail = newNode

    def insert_before(self, key, val):
        current = self.head
        while current is not None:
            if current.info == key:
                newNode = Node(val)
                if current.prev is None:
                    newNode.next = current
                    current.prev = newNode
                    self.head = newNode
                else:
                    current.prev.next = newNode
                    newNode.prev = current.prev
                    current.prev = newNode
                    newNode.next = current
                return
            current = current.next
        print('Key not found')

    def insert_after(self, key, val):
        current = self.head
        while current is not None:
            if current.info == key:
                newNode = Node(val)
                if current.next is None:
                    current.next = newNode
                    newNode.prev = current
                    self.tail = newNode
                else:
                    current.next.prev = newNode
                    newNode.next = current.next
                    newNode.prev = current
                    current.next = newNode
                return
            current = current.next
        print('Key not found')

    def update(self, key, val):
        current = self.head
        while current is not None:
            if current.info == key:
                current.info = val
                return
            current = current.next
        print('Key not found')

    def remove(self, key):
        current = self.head
        while current is not None:
            if current.info == key:
                if current.next is None:
                    current.prev.next = None
                    self.tail = current.prev
                    del current
                elif current.prev is None:
                    current.next.prev = None
                    self.head = current.next
                    del current
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    del current
                return
            current = current.next
        print('Key not found')

    def remove_at_head(self):
        current = self.head
        current.next.prev = None
        self.head = current.next
        del current

    def remove_at_tail(self):
        current = self.head
        while current.next is not None:
            current = current.next
        current.prev.next = None
        self.tail = current.prev
        del current

    def remove_before(self, key):
        current = self.head
        while current is not None:
            if current.info == key:

                if current.prev is None:
                    print('No element before first element')
                
                elif current.prev.prev is None:
                    self.head = current
                    current.prev = None
                    del current.prev
                
                else:
                    current.prev.prev.next = current
                    current.prev = current.prev.prev
                    del current.prev
                return
            current = current.next

    def remove_after(self, key):
        current = self.head
        while current is not None:
            if current.info == key:

                if current.next == None:
                    print('No node after last node')

                elif current.next.next == None:
                    self.tail = current
                    current.next = None
                    del current.next
                    
                else:
                    current.next = current.next.next
                    current.next.next.prev = current
                    del current.next
                return
            current = current.next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.info == key:
                print('Key found')
                return True
            current = current.next
        print('Key not found')
        return False

    def length(self):
        count = 0
        current = self.head
        if current is None:
            print('Empty')
            return 0
        while current is not None:
            count += 1
            current = current.next
        print('Length: ', count)
        return count

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end=' ')
            current = current.next
        print()

def main():
    a = DoublyLinkedList()
    a.insert_at_head(6)
    a.insert_at_head(2)
    a.insert_at_tail(4)
    a.insert_before(2, 1)
    a.insert_after(4, 5)
    a.update(6, 3)
    a.remove_at_head()
    a.remove_at_tail()
    # a.remove_before(4)
    a.remove_after(2)
    a.display()
    a.length()
    # a.search(1)

main()
class Node:
    def __init__(self, val=None) -> None:
        self.info = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_head(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def insert_at_tail(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
        temp.next = newNode

    def insert_before(self, key, value):
        newNode = Node(value)
        current = self.head

        while current.next is not None:
            if current.next.info == key:
                newNode.next = current.next
                current.next = newNode
                break
            current = current.next

        if current.next is None:
            raise KeyError("Key not found in the linked list")

    def insert_after(self, key, value):
        newNode = Node(value)
        current = self.head
        while current is not None:
            if current.info == key:
                temp = current.next
                current.next = newNode
                newNode.next = temp
            current = current.next

    def search(self, key):
        current = self.head
        while current is not None:
            if current.info == key:
                print('Found')
                return 0
            current = current.next
        print('Not Found')
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end=' ')
            current = current.next

    def remove_at_head(self):
        if self.head is None:
            print('List is empty')
        temp = self.head 
        self.head = temp.next
        del temp

    def removeKthNode(self, k):
        count = 1
        current = self.head
        prev = self.head
        if k == 1:
            self.remove_at_head()
        while current is not None:
            if count == k:
                prev.next = current.next
                del current
                return True
            prev = current
            current = current.next
            count += 1
        return False
    

if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_at_head(2)
    obj.insert_at_head(3)
    obj.insert_at_tail(9)
    obj.insert_before(2, 5)
    obj.insert_after(9,1)
    # obj.search(9)
    obj.display()
    print()
    obj.removeKthNode(2)
    obj.display()
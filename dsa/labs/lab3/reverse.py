class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def display_list(self):
        if self.head is None:
            print('List is empty')
        current_node = self.head 
        while current_node is not None:
            print(current_node.data,end=' ')
            current_node = current_node.next
        print()

    def rec_rev(self):
        prev = self.head
        current = prev.next
        helper_recursive_reverse(self, prev, current)
        prev.next = None

def helper_recursive_reverse(obj, prev, current):
    if current == None:
        obj.head = prev
        return
    helper_recursive_reverse(obj, prev.next, current.next)
    current.next = prev

obj = LinkedList()
obj.insert_at_head(1)
obj.insert_at_tail(2)
obj.insert_at_tail(3)
obj.insert_at_tail(4)
obj.display_list()
obj.rec_rev()
obj.display_list()
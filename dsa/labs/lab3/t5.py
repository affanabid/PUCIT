class Node:
    def __init__(self , data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def insert_after(self, key, value):
        newNode = Node(value)
        current = self.head
        while current is not None:
            if current.data == key:
                temp = current.next
                current.next = newNode
                newNode.next = temp
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()
    
    def remove_duplicates(self):
        if not self.head:
            return self.head
    
        seen = []
        seen.append(self.head.data)
        prev = self.head
        current = self.head.next
    
        while current:
            if current.data in seen:
                # Remove the duplicate node
                prev.next = current.next
            else:
                seen.append(current.data)
                prev = current
            current = current.next
        return self.head

    def combine(self,list1,list2):
        self.head=list1.head

        current=list1.head
        while current.next is not None:
            current=current.next
        current.next=list2.head

    def reverse(self):
        current = self.head.next
        prev = self.head
        change_val = None
        while current is not None:
            prev.next = change_val
            change_val = prev
            prev = current
            current = current.next
        prev.next=change_val
        self.head = prev
    
    def rec_rev(self):
        new_list = LinkedList()
        current = self.head
        l = helper_recursive_reverse(new_list, current)
        l.display()

def helper_recursive_reverse(l, current):
    if current is None:
        return l
    l.insert_at_head(current)
    return helper_recursive_reverse(l, current.next)

    # def rec_rev(self):
        # helper_reverse_recursive(self.head)

# def helper_reverse_recursive(head):

#     if head is None or head.next is None:
#         return head

#     reversed_head = helper_reverse_recursive(head.next)
#     head.next.next = head
#     head.next = None

#     return reversed_head
def main():
    list1 = LinkedList()
    list1.insert_at_head(2)
    list1.insert_at_head(4)
    list1.insert_at_head(3)
    list1.insert_at_head(7)
    list1.display()
    list1.rec_rev()
    # list1.reverse()
    # list1.remove_duplicates()
    list1.display()
    # print()
    list2 = LinkedList()
    list2.insert_at_head(9)
    list2.insert_at_head(5)
    # list2.display()

    list3 = LinkedList()
    list3.combine(list1, list2)
    # list3.display()
    
main()
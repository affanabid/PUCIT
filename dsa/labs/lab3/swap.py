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

    def swap(self):
        if self.head == None:
            return self.head
        elif self.head.next is None:
            return self.head
        else:
            current1 = self.head
            current2 = current1.next
            self.head = current2
            while current2 is not None:
                temp = current2.next
                current2.next = current1
                current1.next = temp
                if current1.next is None or current1.next.next is None:
                    break
                current2 = current2.next.next.next
                new_temp = current1.next
                current1.next = current2
                current1 = new_temp

    def removeDuplicates(self):
        current1 = Node(None)
        current2 = self.head
        while current1 is not None and current2 is not None:
            if current2 != current2.next:
                current1.next = current2
                current1 = current2
                current2 = current2.next
            else:
                while current2 == current2.next:
                    current2 = current2.next
                current2 = current2.next

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

def add_two_numbers(l1,l2):
    current1 = l1.head
    current2 = l2.head
    result = []
    carry = 0
    while current1 is not None and current2 is not None:
        if current1 is None:
            current1.data = 0
        if current2 is None:
            current2.data = 0
        sum = current1.data + current2.data + carry
        carry = 0
        if sum > 9:
            carry = 1
            result.append(sum-10)
            if current1.next is None or current2.next is None:
                result.append(1)
            
        else:
            result.append(sum)
        current1 = current1.next
        current2 = current2.next
    return result


def main():
    obj= LinkedList()
    obj.insert_at_tail(1)
    obj.insert_at_tail(2)
    obj.insert_at_tail(3)
    obj.insert_at_tail(4)
    obj.display_list()
    obj.rec_rev()
    obj.display_list()

    # obj.removeDuplicates()
    obj2 = LinkedList()
    obj2.insert_at_head(9)
    obj2.insert_at_tail(9)
    obj2.insert_at_tail(9)
    obj2.insert_at_tail(9)
    # obj2.display_list()
    # print(add_two_numbers(obj, obj2))

main()
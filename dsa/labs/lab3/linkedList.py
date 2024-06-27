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

    def insert_before(self , key , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

    def insert_after(self , key , val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            if temp.data == key:
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next

    def update(self, key ,val):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                temp.data = val
                return
            temp = temp.next
            
    def search(self, val):
        temp = self.head
        while temp is not None:
            if temp.data == val:
                print('Key is present in list')
                return    
            temp = temp.next
        print('key is not present')

    def remove_at_head(self):
        if self.head is None:
            print('List is empty')
        temp = self.head 
        self.head = temp.next
        del temp

    def remove_at_tail(self):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        temp2 = self.head
        while temp.next is not None:
            temp2 = temp
            temp = temp.next
        del temp
        temp2.next = None

    def remove_before(self, key):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        temp2 = self.head
        while temp.next is not None:
            if temp.next.data == key:
                temp2.next = temp.next
                del temp
                return
            temp2 = temp
            temp = temp.next

    def remove_after(self, key):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        temp2 = self.head
        while temp.next is not None:
            if temp.data == key:
                temp.next = temp2.next
                del temp2
                return
            temp = temp.next
            temp2 = temp.next
            
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
    
    def length(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def addTwoNumbers(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                digit1 = l1.val
            else:
                digit1 = 0
            if l2:
                digit2 = l2.val
            else:
                digit2 = 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = Node(digit)
            tail.next = newNode
            tail = tail.next

            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        result = dummy.next
        dummy.next = None
        return result
    
    def padList(self, head, padding):
        new_head = head
        for i in range(padding):
            newNode = Node(0)
            newNode.next = new_head
            new_head = newNode
        return new_head
    
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

    def recursive_reverse(self):
        current = self.head
        helper_recursive(self, current)

    
    def merge(self, list1, list2):
        while list2:
            nextNode = list1.next
            list1.next = list2
            list1 = list2
            list2 = nextNode

def helper_recursive(obj, current, prev=None):
    if current.next is None:
        obj.head = current
        current.next = prev
        return
    helper_recursive(obj, current.next, current)
    current.next = prev

    
    def middle(self):
        current1 = self.head
        current2 = self.head
        while current2 is not None and current2.next is not None:
            current1 = current1.next
            current2 = current2.next.next
        print(current1.data)
    
    def reverse(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        nextNode = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev

# def merge(list1, list2):
#     new = LinkedList()
#     current1 = list1.head
#     current2 = list2.head
#     while current1 or current2:
#         if current1:
#             new.insert_at_tail(current1.data)
#             current1 = current1.next
#         if current2:
#             new.insert_at_tail(current2.data)
#             current2 = current2.next
#     return new
        
            
def main():
    obj= LinkedList()
    obj.insert_at_tail(9)
    obj.insert_at_tail(7)
    obj.insert_at_tail(4)
    obj.insert_at_tail(2)

    # obj.insert_at_tail(2)
    # obj.insert_at_tail(3)
    # obj.insert_at_tail(4)
    o = LinkedList()
    o.insert_at_tail(1)
    o.insert_at_tail(3)
    o.insert_at_tail(8)

    # obj.search(7)
    # obj.remove_at_head()
    # obj.remove_at_tail()
    # obj.display_list()
    # obj.remove_before(8)
    # obj.display_list()
    # obj.remove_after(9)

    obj.display_list()
    o.display_list()
    obj.merge(obj.head, obj.head)
    # print(o.length(obj.head))
    # obj.addTwoNumbers(obj.head, o.head)

    # obj.swap()
    obj.display_list()
        
main()
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    #         current1 = temp1
    #         current2 = temp2

    #     # Update the head of the calling object's list
    #     self.head = list1.head
    #     # Empty the input lists
    #     list1.head = None
    #     list2.head = None
        
    def append(self, info):
        new_node = Node(info)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.info, end=' ')
            current = current.next
        print()

# Example usage:
if __name__ == "__main__":
    # Create two linked lists
    list1 = LinkedList()
    list1.append(2)
    list1.append(6)
    list1.append(4)
    list1.display()

    list2 = LinkedList()
    list2.append(8)
    list2.append(1)
    list2.append(3)
    list2.display()

    # Create an empty linked list
    list3 = LinkedList()

    # Shuffle merge the two lists
    list3.shuffleMerge(list1, list2)

    # Display the shuffled merged list
    list3.display()

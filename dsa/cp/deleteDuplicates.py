# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        pointer = dummy
        prev = None
        current = head
        while current:
            if prev.val == current.val:
                prev = current
                current = current.next
            else:
                if current.val == current.next.val:
                    while current and current.next and current.val == current.next.val:
                        prev = current
                        current = current.next
                else:
                    newNode = ListNode(current.val)
                    pointer.next = newNode
                    pointer = newNode
        new_head = dummy.next
        dummy.next = None
        return new_head

# 206. Reverse Linked List 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        node = head
        previous = None

        # Case for empty linked list
        if node == None:
            return node
                
        while True:

            if node.next == None:
                node.next = previous
                break

            next = node.next
            node.next = previous
            previous = node
            node = next

        return node

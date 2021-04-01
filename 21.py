# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        l1_node = l1
        l2_node = l2
                
        #print(f"Initial l1_node is {l1_node.val}")
        #print(f"Initial l2_node is {l2_node.val}")
        
        if l1_node == None and l2_node == None:
            return l1_node
        
        if l1_node == None:
            print("merged_node starts as l2_node")
            merged_node = l2_node
            l2_node = l2_node.next

        elif l2_node == None:
            print("merged_node starts as l1_node")
            merged_node = l1_node
            l1_node = l1_node.next

        elif l1_node.val < l2_node.val:
            print("merged_node starts as l1_node")
            merged_node = l1_node
            l1_node = l1_node.next

        else: 
            print("merged_node starts as l2_node")
            merged_node = l2_node
            l2_node = l2_node.next
        
        head = merged_node
        
        print(f"Setting head to first node: {head.val}")

        while l1_node != None or l2_node != None:      
            if l1_node == None:
                #print(f"Out of l1_nodes so next is {l2_node.val} from l2")
                merged_node.next = l2_node
                l2_node = l2_node.next
            elif l2_node == None:
                #print(f"Out of l2_nodes so next is {l1_node.val} from l1")
                merged_node.next = l1_node
                l1_node = l1_node.next
            elif l1_node.val < l2_node.val:
                #print(f"l1 is next because {l1_node.val} < {l2_node.val}")
                merged_node.next = l1_node
                l1_node = l1_node.next    
            else:
                #print(f"l2 is next as last resort: {l2_node.val}")
                merged_node.next = l2_node
                l2_node = l2_node.next
            
            merged_node = merged_node.next

        return head
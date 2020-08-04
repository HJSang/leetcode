# 24. Swap Nodes in Pairs

# Medium

# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# 
# 
# 
# Example:
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head_next_next=head.next.next
        new_head=head.next
        new_head.next=head
        head.next=self.swapPairs(head_next_next)
        return new_head

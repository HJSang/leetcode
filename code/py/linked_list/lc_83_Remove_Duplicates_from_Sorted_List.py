# 83. Remove Duplicates from Sorted List

# Easy

# Given a sorted linked list, delete all duplicates such that each element appear only once.
# 
# Example 1:
# 
# Input: 1->1->2
# Output: 1->2
# Example 2:
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy=ListNode(head.val-1)
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if prev.val == cur.val:
                prev.next=prev.next.next
                cur = cur.next
            else:
                prev=prev.next
                cur=cur.next
        return dummy.next


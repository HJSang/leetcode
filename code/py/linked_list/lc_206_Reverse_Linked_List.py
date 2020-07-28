# 206. Reverse Linked List

# Easy


# Reverse a singly linked list.
# 
# Example:
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iterative way
        prev_node = None
        while head:
            head_next = head.next
            head.next = prev_node
            prev_node = head
            head = head_next
        return prev_node


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive way
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

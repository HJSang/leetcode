# 2. Add Two Numbers

# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example:
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        add  = 0
        while l1 or l2:
            if l1 and l2:
                two_sum = l1.val+l2.val
                val, add = (two_sum+add) % 10, (two_sum+add) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val, add = (l1.val+add) % 10, (l1.val+add) // 10
                l1 = l1.next
            else:
                val, add = (l2.val+add) % 10, (l2.val+add) // 10
                l2 = l2.next
            node.next = ListNode(val)
            node=node.next

        if add:
            node.next = ListNode(add)
        return head.next


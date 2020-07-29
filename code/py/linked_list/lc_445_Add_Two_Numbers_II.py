# 445. Add Two Numbers II

# Medium

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1,s2=[],[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        add = 0
        res = []
        while s1 or s2:
            if s1 and s2:
                total = s1.pop()+s2.pop()+add
            elif s1:
                total = s1.pop()+add
            else:
                total = s2.pop()+add
            res.append(total%10)
            add = total//10
        if add:
            res.append(add)
        dummy = ListNode(0)
        head = dummy
        while res:
            dummy.next = ListNode(res.pop())
            dummy = dummy.next
        return head.next





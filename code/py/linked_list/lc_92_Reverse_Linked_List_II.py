# 92. Reverse Linked List II

# Medium

# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # special case
        if m == n:
            return head
        # dummy node
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        # find the node before the starting node
        for _ in range(m-1):
            pre = pre.next
        # reverse [m,n]
        last = None
        cur = pre.next
        for _ in range(n-m+1):
            next_node = cur.next
            cur.next = last
            last = cur
            cur = next_node
        # connect two parts
        pre.next.next=cur
        pre.next=last
        return dummy.next






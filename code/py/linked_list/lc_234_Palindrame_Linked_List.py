# 234. Palindrome Linked List

# Easy

# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# Input: 1->2
# Output: false
# Example 2:
# 
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # revser the second half
        prev = None
        while slow:
            slow_next = slow.next
            slow.next=prev
            prev=slow
            slow=slow_next
        head2=prev
        while head2:
            if head2.val!=head.val:
                return False
            head2=head2.next
            head=head.next
        return True

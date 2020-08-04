# 148. Sort List

# Medium

# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Merge sort
        if not head or not head.next:
            return head
        # find the middle and the node before middle node
        prev, slow, fast = head, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # break into two lists
        prev.next = None
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        return self.mergeSort(head1,head2)
    def mergeSort(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1=l1.next

            else:
                dummy.next = l2
                l2=l2.next
            dummy=dummy.next
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        return head.next

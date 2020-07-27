# 23. Merge k Sorted Lists

# Hard

# Add to List
# 
# Share
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# 
# Example:
# 
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # divide and conquer
        if not lists:
            return
        n=len(lists)
        if n==1:
            return lists[0]
        mid = n//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge2Lists(left, right)
    def merge2Lists(self,l1,l2):
        dummy=ListNode(0)
        head=dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        if l1:
            dummy.next=l1
        if l2:
            dummy.next=l2
        return head.next

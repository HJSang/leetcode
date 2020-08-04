# 109. Convert Sorted List to Binary Search Tree

# Medium

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# 
# Example:
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev=slow=fast=head
        # find the node prior to the middle node
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        root=TreeNode(slow.val)
        prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root





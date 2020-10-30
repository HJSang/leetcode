# 230. Kth Smallest Element in a BST
# Medium
# 
# 3089
# 
# 75
# 
# Add to List
# 
# Share
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# 
#  
# 
# Example 1:
# 
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
# 
#  
# 
# Constraints:
# 
# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums=self.inorder(root)
        return nums[k-1]
    def inorder(self, root):

#         1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then
#      a) Pop the top item from stack.
#      b) Print the popped item, set current = popped_item->right
#      c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.

        stack = []
        trace = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            if not node and stack:
                node = stack.pop()
                trace.append(node.val)
                node = node.right
        return trace




        # if not root:
        #     return
        # self.inorder(root.left, trace)
        # trace.append(root.val)
        # self.inorder(root.right, trace)


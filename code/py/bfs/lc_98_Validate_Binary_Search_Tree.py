# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:
#    2
#   / \
#  1   3

# Input: [2,1,3]
# Output: true

# Example 2:
#    5
#   / \
#  1   4
#     / \
#    3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Idea: Recursive way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkValidBST(root,  float('inf'), -float('inf'))
    def checkValidBST(self, root: TreeNode, max_val, min_val) ->bool:
        if not root:
            return True
        if root.val>=max_val or root.val<=min_val:
            return False
        return self.checkValidBST(root.left, root.val, min_val) and self.checkValidBST(root.right, max_val, root.val)
 


# Binary Tree Inorder Traversal 
def inorderTraversal(root: TreeNode):
  ans = []
  if not root:
    return ans
  stack = []
  while root or stack:
    while root:
      stack.append(root)
      root = root.left
    root = stack.pop()
    ans.append(root.val)
    root = root.right
  return ans      


# Use Inorder Traversal 
def IsValidBST(root: TreeNode) -> bool:
  if not root:
    return True
  stack = []
  pre = None
  while root or stack:
    while root:
      stack.append(root)
      root = root.left
    root = stack.pop()
    if not pre and root.val <= pre.val:
      return False
    pre = root
    root = root.right
  return True    

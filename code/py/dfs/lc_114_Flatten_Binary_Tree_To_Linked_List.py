# 114. Flatten Binary Tree to Linked List

# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
# 
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def __init__(self):
    self.prev = None
  def flatten(self, root:TreeNode) ->None:
    if not root:
      return None
    self.flatten(root.right)
    self.flatten(root.left)
    root.right = self.prev
    root.left = None
    self.prev = root


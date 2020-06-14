# 103. Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between)

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#    3
#   / \
#  9  20
#    /  \
#   15   7
#
# return its zigzag level order traversal as:

#[
#  [3],
#  [20,9],
#  [15,7]
#]

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []
    res, level, direction = [], [root], 1
    while level:
      res.append([n.val for n in level][::direction])
      direction *= -1
      level = [kid for node in level for kid in (node.left, node.right) if kid]
    return res

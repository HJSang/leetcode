# 113. Path Sum II
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
# 
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS

class Solution:
  def pathSum(self, root:TreeNode, sum:int)-> List[List[int]]:
    if not root:
      return []
    res = []
    self.dfs(root,sum, [], res)
    return res

  def dfs(self, root, sum, ls, res):
    if not root.left and not root.right and root.val == sum:
      ls.append(root.val)
      res.append(ls)
    if root.left:
      self.dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
      self.dfs(root.right, sum-root.val, ls+[root.val], res)

# BFS using stack 
class Solution:
  def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    if not root:
      return []
    res = []
    stack = [(root, root.val, [root.val])]
    while stack:
      cur, val, ls = stack.pop()
      if not cur.left and not cur.right and val == sum:
        res.append(ls)
      if cur.right:
        stack.append((cur.right, val+cur.right.val, ls+[cur.right.val]))
      if cur.left:
        stack.append((cur.left, val+cur.left.val, ls+[cur.left.val]))
    return res

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 


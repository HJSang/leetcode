# 366. Find Leaves of Binary Tree

# Given a binary Tree, collect  a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty

# Example:
# Input: [1,2,3,4,5]
#   
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# 
# Output: [[4,5,3],[2],[1]]
#  
# 
# Explanation:
# 
# 1. Removing the leaves [4,5,3] would result in this tree:
# 
#           1
#          / 
#         2          
#  
# 
# 2. Now removing the leaf [2] would result in this tree:
# 
#           1          
#  
# 
# 3. Now removing the leaf [1] would result in the empty tree:
# 
#           []  

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use Node height
# node height of leaf is 0

class Solution:
  def findLeaves(self, root: TreeNode) -> List[List[int]]:
    # node height 
    def dfs(node):
      if not node:
        return -1
      i = 1 + max(dfs(node.left)m dfs(node.right))
      if i == len(out):
        out.append([])
      out[i].append(node.val)
      return i
    out = []
    dfs(root)
    return out


      
       

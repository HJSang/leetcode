# 1214. Two Sum BSTs
# Given two binary search trees, return True if and only if
# there is a node in the first tree and a node in the second
# tree whose values sum up to a given integer target.

# Example 1:
# Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
# Output: true
# Explanation: 2 and 3 sum up to 5.

# Example 2:
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# Output: false
# 
# Constraints:
# Each tree has at most 5000 nodes.
# -10^9 <= target, node.val <= 10^9

# find the leftmost node tree1 and right most of tree2
# if the sum of two nodes < target, move the left most node to its right
# if the sum of tow nodes > target, move the right most node to its left.

class Solution:
  def twoSumBST(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
    stack1, stack2 = [], []
    while True:
      while root1:
        stack1.append(root1)
        root1 = root1.left
      while root2:
        stack2.append(root2)
        root2 = root2.right
      if not stack1 or not stack2: break
      if stack1[-1].val + stack2[-1].val == target:
        return True
      elif stack1[-1].val + stack2[-1].val < target:
        root1 = stack1.pop().right
      else:
        root2 = stack2.pop().left
    return False 

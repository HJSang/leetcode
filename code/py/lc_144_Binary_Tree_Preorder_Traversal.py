# 144. Binary Tree Preorder Traversal 
# Given a binary tree, return the preorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Idea: 
# Using stack 
# since the preorder traversal is  root->left->right
# Hence, push right, left and node to the stack

class Solution:
  def preorderTraversal(self, root:TreeNode) -> List[int]:
    if not root:
      return []
    stack, ans = [root], []
    while stack:
      node = stack.pop()
      if node:
        stack.append(node.right)
        stack.append(node.left)
        ans.append(node.val)
    return ans


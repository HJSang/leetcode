# 199. Binary Tree Right Side View
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom
# Example:
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Idea1: breath traversal 

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack[-1]
            ans.append(node.val)
            next_stack = []
            for i in stack:
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
            stack = next_stack
        return ans 


# Idea2: DFS recursively
class Solution:
  def rightSideView(self, root):
    res = []
    self.dfs(root,0,res)
    return [x[0] for x in res]
  def dfs(self,root,level,res):
    if root:
      if len(res)< level+1:
        res.append([])
      res[level].append(root.val)
      self.dfs(root.right,level+1,res)
      self.dfs(root.left,level+1,res)                




# Idea3: DFS + Stack
class Solution:
  def rightSideView(self,root):
    res, queue = [], [(root,0)]
    while queue:
      curr, level = queue.pop(0)
      if curr:
        if len(res)<level+1:
          res.append([])
        res[level].append(curr.val)
        queue.append((curr.left,level+1))
        queue.append((curr.right, level+1))
    return [x[-1] for x in res]

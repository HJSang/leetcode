# 314. Binary Tree Vertical Order Traversal
# Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.


# Examples 1:
# Input: [3,9,20,null,null,15,7]
#    3
#    /\
#   /  \
#   9  20
#      /\
#     /  \
#    15   7

# Output:

# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]

# Examples 3:
# Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)
#     3
#    /\
#   /  \
#   9   8
#  /\  /\
# /  \/  \
# 4  01   7
#    /\
#   /  \
#   5   2

# Output:

#[
#  [4],
#  [9,5],
#  [3,0,1],
#  [8,2],
#  [7]
#]

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]         

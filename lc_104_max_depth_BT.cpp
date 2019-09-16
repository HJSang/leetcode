/* 104 Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the 
longest path from the root node down to the farthest leaf 
node.

Note: A leaf if a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
*/

// Define a binary Tree
struct TreeNode {
	int val;
	TreenNode *left;
	TreeNode *right;
	TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

/* Solution:
Recursive method:
if empty node:
return 0
else:
d1= maxDepth(root->left);
d2 = maxDepth(root->right);
return max(d1,d2)+1;
*/
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int depth = 0;
        if(root==NULL)
        {
            return 0;
        }
        else
        {
            int d1 = maxDepth(root->left);
            int d2 = maxDepth(root->right);
            return max(d1,d2)+1;
        }
        
    }
};
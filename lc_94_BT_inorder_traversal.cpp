/* 94. Binary Tree Inorder Traversal.
Given a binary tree, return the inorder traversal of its
nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
*/

//useful link:https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

//Recursive Solution
// traversal left tree
// input root val
// traversalright tree
void BT_inorderTraversal(TreeNode* root, vector<int> &r)
{
    if(root==NULL)
    {
        return;
    }
    else
    {
        BT_inorderTraversal(root->left, r);
        r.push_back(root->val);
        BT_inorderTraversal(root->right,r);
    }
}
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> r;
        BT_inorderTraversal(root,r);   
        return r;
    }
};

/* Iterative solution
Using Stack is the way to traverse tree without recursion.
1) Create an empty stack
2) Initilize crurrent node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If Current is NULL and stack is not empty then
  a) Pop the top item from the stack
  b) Print the popped item, set current = poped_item->right
  c) Go to Step 3
5) If current is NULL and stack is empty, then we are done.  
*/

class Solution {
public:
    void left_traverse(stack<TreeNode*>&s, TreeNode* root)
    {
        while(root)
        {
            s.push(root);
            root = root->left;
        }
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> r;
        stack<TreeNode*> s;
        left_traverse(s,root);
        while(!s.empty())
        {
            TreeNode* current = s.top();
            r.push_back(current->val);
            s.pop();
            left_traverse(s,current->right);
        }
        return r;
        
    }
    
};
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1==NULL && t2==NULL) return NULL; // if both trees are empty
        if (t1==NULL) return t2; // if one of them is empty
        if (t2==NULL) return t1;
        
        t1->val = t1->val + t2->val; // just add corresponding t1 and t2
        // and update it into t1
        t1->left = mergeTrees(t1->left,t2->left); // go to left subtree
        t1->right = mergeTrees(t1->right,t2->right); // go to right subtree
        
        return t1;
    }
};

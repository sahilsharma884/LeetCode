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
    int maxDepth(TreeNode* root) {
        if (root == NULL) { return 0; } // If root is empty, return 0
        else {
            int leftsubtree = maxDepth(root->left); // Move to left subtree
            int rightsubtree = maxDepth(root->right); // Move to right subtree
            
            if (leftsubtree > rightsubtree) { return leftsubtree + 1; } // If leftsubtree greater than rightsubtree, then return num of depth from left subtree
            else { return rightsubtree + 1; } // Otherwise return number of depth from right subtree
        }
    }
};

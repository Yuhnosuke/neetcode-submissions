/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) {
            return false;
        }

        if (this.isSameTree(root, subRoot)) {
            return true;
        }

        return this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot);
    }

    public boolean isSameTree(TreeNode node, TreeNode other) {
        if (node == null && other == null) {
            return true;
        }

        if (node == null || other == null) {
            return false;
        }

        if (node.val != other.val) {
            return false;
        }

        return this.isSameTree(node.left, other.left) && this.isSameTree(node.right, other.right);
    }
}

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


    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }

        if (Math.abs(this.dfs(root.left) - this.dfs(root.right)) > 1) {
            return false;
        }

        return this.isBalanced(root.left) && this.isBalanced(root.right);
        
    }

    public int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int left = this.dfs(node.left);
        int right = this.dfs(node.right);

        return 1 + Math.max(left, right);
    }


}

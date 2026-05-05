# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(current_node):
            if not current_node:
                return 0
            
            left = dfs(current_node.left)
            right = dfs(current_node.right)

            self.result = max(self.result, left + right)

            return max(left, right) + 1

        dfs(root)
        return self.result

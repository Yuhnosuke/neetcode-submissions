# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node: Optional[TreeNode], lower: int, higher: int) -> bool:
            if not node:
                return True
            
            if not lower < node.val < higher:
                return False
            
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, higher)
            
        
        return dfs(root, float("-inf"), float("inf"))
            
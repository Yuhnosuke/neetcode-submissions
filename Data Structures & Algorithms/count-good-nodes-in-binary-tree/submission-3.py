# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, curr_max: int):
            if not node:
                return 0
            
            res = 1 if node.val >= curr_max else 0

            curr_max = max(curr_max, node.val)
            
            res += dfs(node.left, curr_max)
            res += dfs(node.right, curr_max)

            return res
        
        return dfs(root, root.val)

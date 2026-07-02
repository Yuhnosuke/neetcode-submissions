# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, curr_max):
            nonlocal res

            if not root:
                return

            curr_max = max(curr_max, root.val)

            if root.left:
                if curr_max <= root.left.val:
                    res += 1
                    dfs(root.left, curr_max)
                else:
                    dfs(root.left, curr_max)
            
            if root.right:
                if curr_max <= root.right.val:
                    res += 1
                    dfs(root.right, curr_max)
                else:
                    dfs(root.right, curr_max)
        
        dfs(root, root.val)
        return res + 1
        
        
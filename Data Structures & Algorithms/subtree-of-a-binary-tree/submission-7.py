# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(node, subRoot):
            if not node and not subRoot:
                return True
            
            if not node or not subRoot:
                return False
            if node.val != subRoot.val:
                return False
            
            return isSameTree(node.left, subRoot.left) and isSameTree(node.right, subRoot.right)


        def dfs(node):
            if not node:
                return False
            
            if isSameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)


        return dfs(root)
        

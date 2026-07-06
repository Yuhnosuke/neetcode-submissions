# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = k
        res = root.val

        def inorder(node):
            nonlocal count
            nonlocal res
            
            if not node:
                return
            
            inorder(node.left)

            count -= 1
            if count == 0:
                res = node.val

            inorder(node.right)
        
        inorder(root)
        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack, q_stack = [], []

        def dfs(node: Optional[TreeNode], stack: List) -> None:
            if not node:
                stack.append(None)
                return
            
            dfs(node.left, stack)
            dfs(node.right, stack)

            stack.append(node.val)
        
        dfs(p, p_stack)
        dfs(q, q_stack)

        if len(p_stack) != len(q_stack):
            return False
        
        for pe, qe in zip(p_stack, q_stack):
            if pe != qe:
                return False
        return True
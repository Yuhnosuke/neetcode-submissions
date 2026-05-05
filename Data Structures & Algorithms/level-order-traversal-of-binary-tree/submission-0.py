# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        answer = []
        queue = deque([root])

        while queue:
            length_in_current_level = len(queue)
            nodes_in_current_level = []
            for _ in range(length_in_current_level):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                nodes_in_current_level.append(node.val)
            answer.append(nodes_in_current_level)

        return answer
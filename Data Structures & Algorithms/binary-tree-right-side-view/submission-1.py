# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:

            num_of_nodes_in_curr_level = len(q)
            
            for i in range(num_of_nodes_in_curr_level):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                if i == num_of_nodes_in_curr_level - 1:
                    res.append(node.val)

        return res

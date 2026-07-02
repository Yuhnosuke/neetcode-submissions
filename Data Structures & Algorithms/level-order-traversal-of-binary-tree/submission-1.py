# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            tmp = []
            num_of_nodes_in_curr_level = len(q)

            for _ in range(num_of_nodes_in_curr_level):                
                node = q.popleft()
                tmp.append(node.val)                    

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(tmp)
        
        return res
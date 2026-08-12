"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        val_to_node = {}

        def clone_node(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            
            if node.val in val_to_node:
                return val_to_node[node.val]

            cloned = Node(node.val)

            val_to_node[node.val] = cloned

            for neighbor in node.neighbors:
                cloned.neighbors.append(clone_node(neighbor))

            return cloned

        return clone_node(node)
        

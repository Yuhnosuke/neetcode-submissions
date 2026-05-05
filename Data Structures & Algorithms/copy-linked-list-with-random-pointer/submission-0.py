"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}
        current = head

        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copied = node_map[current]
            copied.next = node_map[current.next]
            copied.random = node_map[current.random]

            current = current.next

        return node_map[head]
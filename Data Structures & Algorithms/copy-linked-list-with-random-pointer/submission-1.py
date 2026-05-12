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
        original_to_copied = { None: None }
        curr = head

        # copy the nodes
        while curr:
            original_to_copied[curr] = Node(curr.val)
            curr = curr.next
        
        # set the pointers
        curr = head
        while curr:
            copied = original_to_copied[curr]
            copied.next = original_to_copied[curr.next]
            copied.random = original_to_copied[curr.random]
            curr = curr.next
        return original_to_copied[head]


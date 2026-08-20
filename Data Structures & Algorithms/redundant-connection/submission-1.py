class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
        self.num_of_components = n
    
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x: int, y: int) -> bool:
        parent_x, parent_y = self.find(x), self.find(y)

        if parent_x == parent_y:
            return False

        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.ranks[parent_x] < self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union_find = UnionFind(n)

        for u, v in edges:
            if not union_find.union(u - 1, v - 1):
                return [u, v]

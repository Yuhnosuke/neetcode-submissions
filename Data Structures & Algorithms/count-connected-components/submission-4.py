class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
        self.connected_components_count = n
    
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return False
        
        if self.ranks[root_x] > self.ranks[root_y]:
            self.parents[root_y] = root_x
        elif self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = root_y
        else:
            self.parents[root_y] = root_x
            self.ranks[root_x] += 1
        
        self.connected_components_count -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for u, v in edges:
            union_find.union(u, v)
        return union_find.connected_components_count
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

        self.num_of_components -= 1
        return True
    
    def get_num_of_components(self):
        return self.num_of_components

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        union_find = UnionFind(n)

        for u, v in edges:
            if not union_find.union(u, v):
                return False
        return union_find.num_of_components == 1
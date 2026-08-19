class UnionFind:
    
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.ranks = [0] * n
        self.num_of_components = n
        
    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

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

    def getNumComponents(self) -> int:
        return self.num_of_components

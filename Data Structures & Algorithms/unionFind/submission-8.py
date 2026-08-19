class UnionFind:
    
    def __init__(self, n: int):
        self.node_to_parent = { i: i for i in range(n) }
        self.node_to_rank = { i: 0 for i in range(n) }
        self.num_components = n

    def find(self, x: int) -> int:
        if self.node_to_parent[x] != x:
            self.node_to_parent[x] = self.find(self.node_to_parent[x])
        return self.node_to_parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.node_to_rank[root_x] > self.node_to_rank[root_y]:
            self.node_to_parent[root_y] = root_x
        elif self.node_to_rank[root_x] < self.node_to_rank[root_y]:
            self.node_to_parent[root_x] = root_y
        else:
            self.node_to_parent[root_y] = root_x
            self.node_to_rank[root_x] += 1
        
        self.num_components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.num_components
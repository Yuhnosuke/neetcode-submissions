class UnionFind:

    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return False
        
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] += self.rank[y_parent]
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += self.rank[x_parent]
        
        return True
        

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # initialize min_heap
        # (weight, v1, v2)
        min_heap = []
        for u, v, w in edges:
            heapq.heappush(min_heap, (w, u, v))

        # initialize mst
        # (v1, v2, weight)
        mst = []

        # initialize union find instance
        uf = UnionFind(n)
        components = n

        
        while components > 1 and min_heap:
            weight, v1, v2 = heapq.heappop(min_heap)
            
            # detect cycle
            if not uf.union(v1, v2):
                continue
            
            mst.append((v1, v2, weight))
            components -= 1
        
        if components != 1:
            return -1
            
        min_cost = 0
        for v1, v2, w in mst:
            min_cost += w
        return min_cost
        




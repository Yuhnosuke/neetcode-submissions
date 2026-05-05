class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # build adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
        
        visited = set()
        topological_order = []
        path = set()

        # post order dfs
        def dfs(i):
            if i in path:
                return True
            
            if i in visited:
                return False
            
            path.add(i)
            visited.add(i)

            for neighbor in adj[i]:
                if dfs(neighbor):
                    return True
            
            topological_order.append(i)
            path.remove(i)

        for i in range(n):
            # if cycle detected
            if dfs(i):
                return []
        
        topological_order.reverse()
        return topological_order
        


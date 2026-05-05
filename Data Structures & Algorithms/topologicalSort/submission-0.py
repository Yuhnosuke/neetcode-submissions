class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, adj, visited, rec_stack,top_list):
            if node in rec_stack:
                return True

            if node in visited:
                return False
            
            visited.add(node)
            rec_stack.add(node)

            for neighbor in adj[node]:
                if dfs(neighbor, adj, visited, rec_stack, top_list):
                    return True
            
            rec_stack.remove(node)
            top_list.append(node)
            return False

        adj = {}

        for i in range(n):
            adj[i] = []
        
        for u, v in edges:
            adj[u].append(v)


        topological_order = []
        visited = set()
        rec_stack = set()

        for i in range(n):
            if i not in visited:
                if dfs(i, adj, visited, rec_stack, topological_order):
                    return []

        topological_order.reverse()
        return topological_order
        
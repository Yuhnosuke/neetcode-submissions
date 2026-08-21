class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        indegrees = [0] * (n + 1)

        graph = {}
        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            indegrees[v] += 1
            graph[v].append(u)
            indegrees[u] += 1

        q = deque()
        for node in range(1, n + 1):
            if indegrees[node] == 1:
                q.append(node)
        
        # current_index = 0

        while q:
            node = q.popleft()
            indegrees[node] -= 1
            # current_index += 1
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 1:
                    q.append(neighbor)
        
        for u, v in reversed(edges):
            if indegrees[u] == 2 and indegrees[v]:
                return [u, v]
            
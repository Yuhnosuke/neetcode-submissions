class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
              
        dummy_node = -1
        return dfs(0, dummy_node) and len(visited) == n

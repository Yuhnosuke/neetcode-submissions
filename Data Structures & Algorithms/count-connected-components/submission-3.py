class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_of_components = 0
        visited = set()

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(node: int) -> None:
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)


        for i in range(n):
            if i not in visited:
                dfs(i)
                num_of_components += 1
        return num_of_components


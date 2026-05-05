from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
        
        shortest_path = {}
        min_heap = [[0, src]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in shortest_path:
                continue
            
            shortest_path[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest_path:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        
        for node in range(n):
            if node not in shortest_path:
                shortest_path[node] = -1

        return shortest_path

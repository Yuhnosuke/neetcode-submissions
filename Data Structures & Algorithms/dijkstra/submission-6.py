import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # build adj list
        # {0: [], 1: [], ...}
        adj = {}
        for i in range(n):
            adj[i] = []
        
        # src -> (dst, weight)
        # {0: [(1, 10), (2: 3)]}
        for u, v, weight in edges:
            adj[u].append((v, weight))

        # min_heap
        # (w, src)
        min_heap = [(0, src)]
        heapq.heapify(min_heap)

        # shortest
        shortest_path = {}

        while min_heap:

            curr_weight, curr_node = heapq.heappop(min_heap)

            if curr_node in shortest_path:
                continue
            
            shortest_path[curr_node] = curr_weight

            for nei_node, nei_weight in adj[curr_node]:

                if nei_node in shortest_path:
                    continue

                heapq.heappush(min_heap, (curr_weight + nei_weight,nei_node))
            
        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1
        
        return shortest_path
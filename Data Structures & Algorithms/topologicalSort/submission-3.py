class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        dependant_to_dependancy = defaultdict(list)
        for src, dest in edges:
            dependant_to_dependancy[src].append(dest)

        toplogical_sorted = []
        visited = set()
        current_path = set()

        def topological_sort_helper(node: int) -> bool:
            if node in current_path:
                return False
            if node in visited:
                return True

            visited.add(node)
            current_path.add(node)

            for neighbor in dependant_to_dependancy[node]:
                if not topological_sort_helper(neighbor):
                    return False
            
            current_path.remove(node)
            toplogical_sorted.append(node)
            return True

        for i in range(n):
            if not topological_sort_helper(i):
                return []
                
        toplogical_sorted.reverse()
        return toplogical_sorted

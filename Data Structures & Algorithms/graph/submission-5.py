from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        
        if dst not in self.graph:
            self.graph[dst] = set()
    
        self.graph[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        
        if dst not in self.graph[src]:
            return False

        self.graph[src].remove(dst)

        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)
    
    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True

        visited.add(src)
        for neighbor in self.graph.get(src, []):
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True
        return False

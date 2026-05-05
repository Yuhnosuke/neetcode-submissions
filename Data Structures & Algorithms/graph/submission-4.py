from collections import deque

class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = [dst]
        else:
            self.graph[src].append(dst)
        
        if dst not in self.graph:
            self.graph[dst] = []

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        
        if dst not in self.graph[src]:
            return False


        self.graph[src].remove(dst)

        
        
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        
        queue = deque()
        queue.append(src)

        visited = set()
        visited.add(src)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == dst:
                    return True
                
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return False

        


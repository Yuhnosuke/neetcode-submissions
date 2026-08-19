class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        course_to_prerequisites = {c: [] for c in range(numCourses)}

        for c, p in prerequisites:            
            indegree[p] += 1   
            course_to_prerequisites[c].append(p)

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        current_index = 0
        topological_order = []

        while q:
            course = q.popleft()
            topological_order.append(course)
            current_index += 1

            for prerequisite in course_to_prerequisites[course]:
                indegree[prerequisite] -= 1
                if indegree[prerequisite] == 0:
                    q.append(prerequisite)
        
        if current_index != numCourses:
            return []
        topological_order.reverse()
        return topological_order
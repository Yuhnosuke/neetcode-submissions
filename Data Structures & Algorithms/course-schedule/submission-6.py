class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course: int, visited: set) -> bool:
            if course in visited:
                return False
                
            if course in memo:
                return memo[course]
            
            visited.add(course)

            for prerequisite in course_to_prerequisites[course]:
                if not dfs(prerequisite, visited):
                    memo[course] = False
                    return False
            
            visited.remove(course)
            memo[course] = True
            return True

        course_to_prerequisites = defaultdict(list)
        memo = {}

        for c, p in prerequisites:
            course_to_prerequisites[c].append(p)
        
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True
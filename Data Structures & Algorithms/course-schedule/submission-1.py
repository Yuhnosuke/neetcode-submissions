from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        course_prerequisite_map = defaultdict(list)
        
        for course, prerequisite in prerequisites:
            course_prerequisite_map[course].append(prerequisite)
        
        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if course_prerequisite_map[course] == []:
                return True
            
            visited.add(course)

            for prerequisite in course_prerequisite_map[course]:
                if not dfs(prerequisite):
                    return False

            visited.remove(course)
            course_prerequisite_map[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        course_to_prerequisites = defaultdict(list)

        for c, p in prerequisites:
            course_to_prerequisites[c].append(p)

        def dfs(course: int) -> bool:
            if course not in course_to_prerequisites:
                return True
            if course in taken:
                return False
            
            taken.add(course)

            for p in course_to_prerequisites[course]:
                if not dfs(p):
                    return False   
            del course_to_prerequisites[course]          
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

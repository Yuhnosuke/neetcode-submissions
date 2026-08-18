class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prerequisites = defaultdict(list)
        for c, p in prerequisites:
            course_to_prerequisites[c].append(p)

        taken = set()

        def check_prerequisites(course: int) -> bool:
            if course not in course_to_prerequisites:
                return True
            if course in taken:
                return False

            taken.add(course)

            for p in course_to_prerequisites[course]:
                if not check_prerequisites(p):
                    return False
            del course_to_prerequisites[course]
            return True

        for c in range(numCourses):
            if not check_prerequisites(c):
                return False
        return True







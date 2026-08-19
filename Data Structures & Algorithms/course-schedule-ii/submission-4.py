class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_prerequisites = defaultdict(list)
        for c, p in prerequisites:
            course_to_prerequisites[c].append(p)
        
        topological_sorted = []
        current_path = set()
        taken = set()

        def topological_sort(course: int) -> bool:
            if course in current_path:
                return False
            if course in taken:
                return True
            
            current_path.add(course)
            taken.add(course)

            for p in course_to_prerequisites[course]:
                if not topological_sort(p):
                    return False
            
            current_path.remove(course)
            topological_sorted.append(course)
            return True

        for c in range(numCourses):
            if not topological_sort(c):
                return []
        return topological_sorted


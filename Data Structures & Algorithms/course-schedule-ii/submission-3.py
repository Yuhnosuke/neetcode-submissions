from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_prerequisite_map = defaultdict(list)
        for course, prerequisite in prerequisites:
            course_prerequisite_map[course].append(prerequisite)
        
        visited = set()
        def dfs(course: int) -> bool:
            if course in visited:
                return False
            
            if course_prerequisite_map[course] == []:
                if  course not in answer:
                    answer.append(course)
                return True

            visited.add(course)

            for prerequisite in course_prerequisite_map[course]:
                if not dfs(prerequisite):
                    return False
            
            answer.append(course)
            visited.remove(course)
            course_prerequisite_map[course] = []

            return True


        answer = []
        for course in range(numCourses):
            if not dfs(course):
                return []

        return answer
        
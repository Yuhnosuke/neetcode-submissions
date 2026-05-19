class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circular_students, square_students = 0, 0

        for student in students:
            if student == 1:
                square_students += 1
            else:
                circular_students += 1
        
        for sandwiche in sandwiches:
            if sandwiche == 1 and square_students == 0:
                return circular_students
            if sandwiche == 0 and circular_students == 0:
                return square_students
            if sandwiche == 1:
                square_students -= 1
            else:
                circular_students -= 1
        return 0
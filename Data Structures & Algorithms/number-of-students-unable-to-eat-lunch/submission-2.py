class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length = len(students)
        answer = length
        q = deque(students)

        for sandwich in sandwiches:
            count = 0
            while count < length and q[0] != sandwich:
                q.append(q.popleft())
                count += 1

            if q[0] == sandwich:
                q.popleft()
                answer -= 1
            else:
                break

        return answer

from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash_map[key]

        answer = ""
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                answer = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return answer

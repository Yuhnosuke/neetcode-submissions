import heapq
from collections import defaultdict, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency_map = defaultdict(int)
        for task in tasks:
            task_frequency_map[task] += 1
        
        max_heap = [-frequency for frequency in task_frequency_map.values()]
        heapq.heapify(max_heap)

        queue = deque()
        current_time = 0

        while max_heap or queue:
            current_time += 1
            
            if max_heap:
                task_before_process = -heapq.heappop(max_heap)
                processed_task = task_before_process - 1
                if processed_task:
                    queue.append((-processed_task, current_time + n))
            
            if queue and current_time == queue[0][1]:
                waiting_task = queue.popleft()
                heapq.heappush(max_heap, waiting_task[0])
                
        return current_time
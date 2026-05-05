import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            
            diff = first - second
            if diff > 0:
                heapq.heappush(heap, -diff)
        
        return -heap[0] if len(heap) else 0



        
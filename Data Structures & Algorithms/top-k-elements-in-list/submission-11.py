class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 0
            num_to_freq[num] += 1
        
        heap = []
        for num in num_to_freq.keys():
            heapq.heappush(heap, (num_to_freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer
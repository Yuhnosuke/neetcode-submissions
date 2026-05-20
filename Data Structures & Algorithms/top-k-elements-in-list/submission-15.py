class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count frequency with hashmap
        # 2. heap
        # 3. bucket sort
        
        # (freq, value)
        
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num, 0)
        
        min_heap = []
        for n, f in num_to_freq.items():
            heapq.heappush(min_heap, (f, n))
        
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return list(map(lambda x: x[1], min_heap))


            
            


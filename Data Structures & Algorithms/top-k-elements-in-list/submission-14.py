class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count frequency with hashmap
        # 2. heap
        # 3. bucket sort
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num, 0)
        return list(map(lambda x: x[0], sorted(num_to_freq.items(), key=lambda x: x[1], reverse=True)))[:k]


            
            


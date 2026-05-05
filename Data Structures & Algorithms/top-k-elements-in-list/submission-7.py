class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 0    
            num_to_freq[num] += 1
        
        return list(map(lambda x: x[0], sorted(num_to_freq.items(), reverse=True, key=lambda x: x[1])[:k]))


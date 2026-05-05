class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        
        return list(map(lambda x: x[0], sorted(num_to_freq.items(),key=lambda x: x[1], reverse=True)))[:k]
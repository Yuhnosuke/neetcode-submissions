class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num, 0)
        
        freq_values = [[] for _ in range(len(nums) + 1)]
        for num, freq in num_to_freq.items():
            freq_values[freq].append(num)

        ans = []
        for i in range(len(freq_values) - 1, 0, -1):
            for num in freq_values[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                curr_length = 0
                while num + curr_length in num_set:
                    curr_length += 1 
                longest = max(longest, curr_length)
        return longest
                

        
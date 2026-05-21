class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                curr_len = 1
                while num + curr_len in num_set:
                    curr_len += 1
                ans = max(ans, curr_len)
        return ans

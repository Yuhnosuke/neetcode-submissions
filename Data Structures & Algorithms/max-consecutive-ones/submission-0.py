class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        n = len(nums)
        for i in range(n):
            curr_max = 0
            while i < n and nums[i] == 1:
                curr_max += 1
                i += 1
            max_so_far = max(max_so_far, curr_max)
        
        return max_so_far


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums: List[int]) -> int:
            max_before_last, max_so_far = 0, 0
            for amount in nums:
                rub = amount + max_before_last
                skip = max_so_far
                max_before_last = skip
                max_so_far = max(rub, skip)
            return max_so_far
            
        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[1:]), dp(nums[:-1]))

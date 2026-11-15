class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = 1, 1
        for num in nums:
            tmp = curr_max * num
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(tmp, curr_min * num, num)
            res = max(res, curr_max)
        return res

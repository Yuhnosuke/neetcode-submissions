class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]
        
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suf
            suf *= nums[i]
        return output
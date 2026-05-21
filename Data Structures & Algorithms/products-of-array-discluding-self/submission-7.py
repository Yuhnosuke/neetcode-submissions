class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        prefix = 1
        for p in range(len(nums)):
            ans[p] *= prefix
            prefix *= nums[p]
        
        suffix = 1
        for s in range(len(nums) - 1, -1, -1):
            ans[s] *= suffix
            suffix *= nums[s]
        
        return ans


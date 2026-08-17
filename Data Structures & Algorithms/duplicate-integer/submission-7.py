class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:            
            return False
        
        nums.sort()
        p = 1
        
        while p < len(nums):
            if nums[p] == nums[p - 1]:
                return True
            p += 1
        return False

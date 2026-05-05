class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            prev, curr = nums[i - 1], nums[i]

            if curr == prev:
                return True
        
        return False
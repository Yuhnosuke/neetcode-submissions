class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        nums.sort()
        ans = 0

        for i in range(1, len(nums)):
            curr = 1
            while i < len(nums) and nums[i] == nums[i - 1] + 1:
                curr += 1
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
            ans = max(ans, curr)
        return ans

         

           
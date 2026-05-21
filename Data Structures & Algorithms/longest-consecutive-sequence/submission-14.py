class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        nums.sort()
        ans = 1

        for i in range(1, len(nums)):
            curr = 1
            while i < len(nums) and nums[i] == nums[i - 1] + 1:
                curr += 1
                i += 1
                while i < len(nums) and nums[i] == nums[i - 1]:
                    i += 1
            ans = max(ans, curr)
        return ans

         

           
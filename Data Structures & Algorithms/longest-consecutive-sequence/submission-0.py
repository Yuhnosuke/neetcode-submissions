class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        global_longest = 0
        for num in nums:
            local_longest = 0
            if not num - 1 in numSet:                
                while num + local_longest in numSet:
                    local_longest += 1
            global_longest = max(global_longest, local_longest)
        return global_longest
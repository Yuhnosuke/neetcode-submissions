class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False

        target = total // 2

        def dfs(i, current_target):
            if current_target < 0:
                return False

            if i >= len(nums):
                return current_target == 0

            return dfs(i + 1, current_target) or dfs(i + 1, current_target - nums[i])


        return dfs(0, target)
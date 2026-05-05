class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, current_sum):
            if i == len(nums):
                if current_sum == target:
                    return 1
                return 0

            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            negative_case = dfs(i + 1, current_sum - nums[i])
            positive_case = dfs(i + 1, current_sum + nums[i])
            answer = negative_case + positive_case

            memo[(i, current_sum)] = answer
            return answer
        
        
        memo = {}
        return dfs(0, 0)
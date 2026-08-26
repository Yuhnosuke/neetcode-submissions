class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dp(i: int, memo: dict) -> int:
            if i in memo:
                return memo[i]

            if i == 0 or i == 1:
                return 0
        
            one_step_prev = cost[i - 1] + dp(i - 1, memo)
            two_step_prev = cost[i - 2] + dp(i - 2, memo)
            memo[i] = min(one_step_prev, two_step_prev)
            return memo[i]

        memo = {}
        return dp(len(cost), memo)


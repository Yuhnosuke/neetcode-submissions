class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dp(i, curr):
            if i == len(profit):
                return 0

            if (i, curr) in memo:
                return memo[(i, curr)]       
            
            memo[(i, curr)] = dp(i + 1, curr)

            new_capacity = curr - weight[i]
            if new_capacity >= 0:
                p = profit[i] + dp(i, new_capacity)
                memo[(i, curr)] = max(memo[(i, curr)], p)

            
            return memo[(i, curr)]

        memo = {}
        return dp(0, capacity)
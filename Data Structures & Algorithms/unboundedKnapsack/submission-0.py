class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dp(i, curr):
            if i == len(profit):
                return 0
            
            # skip
            max_profit = dp(i + 1, curr)

            # take
            new_capacity = curr - weight[i]
            if new_capacity >= 0:
                p = profit[i] + dp(i, new_capacity)
                max_profit = max(max_profit, p)
            
            return max_profit

        return dp(0, capacity)
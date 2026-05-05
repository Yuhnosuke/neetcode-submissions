class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dp(i, curr_profit, curr_capacity):
            if i == len(profit):
                return curr_profit
            
            # not include
            not_include = dp(i + 1, curr_profit, curr_capacity)

            # include
            include = dp(i + 1, curr_profit + profit[i], curr_capacity - weight[i]) if curr_capacity - weight[i] >= 0 else 0

            return max(not_include, include)
        
        return dp(0, 0, capacity)

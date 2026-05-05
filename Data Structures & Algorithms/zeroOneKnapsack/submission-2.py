class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dp(i, curr_profit, curr_capacity):
            if curr_capacity < 0:
                return 0
                
            if i == len(profit):
                return curr_profit
            

            # not include
            not_include = dp(i + 1, curr_profit, curr_capacity)

            # include
            include = dp(i + 1, curr_profit + profit[i], curr_capacity - weight[i])

            return max(not_include, include)
        
        return dp(0, 0, capacity)

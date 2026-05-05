class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dp(i, curr_capacity):
            if i == len(profit):
                return 0
            
            not_include = dp(i + 1, curr_capacity)
            include = profit[i] + dp(i + 1, curr_capacity + weight[i]) if curr_capacity + weight[i] <= capacity else 0

            return max(not_include, include)
        
        return dp(0, 0)
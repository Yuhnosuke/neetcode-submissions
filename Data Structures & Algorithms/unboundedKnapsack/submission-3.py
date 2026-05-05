class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # i番目までのitemでcurr_capacityで作れる最大profit
        def dp(i: int, curr_capacity: int) -> int:
            if i == len(profit):
                return 0
            
            if (i, curr_capacity) in memo:
                return memo[(i, curr_capacity)]
            
            not_take = dp(i + 1, curr_capacity)

            take = 0
            if curr_capacity - weight[i] >= 0:
                take = profit[i] + dp(i, curr_capacity - weight[i])

            memo[(i, curr_capacity)] = max(not_take, take)
            return memo[(i, curr_capacity)]
        
        memo = {}
        return dp(0, capacity)
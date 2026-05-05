class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dp(i, curr_capacity, memo):
            if i == len(profit):
                return 0
            
            if memo[i][curr_capacity] != -1:
                return memo[i][curr_capacity]
            
            not_include = dp(i + 1, curr_capacity, memo)
            include = profit[i] + dp(i + 1, curr_capacity + weight[i], memo) if curr_capacity + weight[i] <= capacity else 0

            memo[i][curr_capacity] = max(not_include, include)

            return memo[i][curr_capacity]
        
        memo = [[-1] * (capacity + 1) for _ in range(len(profit))]
        return dp(0, 0, memo)
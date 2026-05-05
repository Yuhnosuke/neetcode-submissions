class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def dp(i, curr_capacity, memo):
            if i == len(profit):
                return 0
            
            if memo[i][curr_capacity] != -1:
                return memo[i][curr_capacity]
            
            # include
            include = profit[i] + dp(i + 1, curr_capacity - weight[i], memo) if curr_capacity - weight[i] >= 0 else 0

            # not include
            not_include = dp(i + 1, curr_capacity, memo)

            memo[i][curr_capacity] = max(include, not_include)

            return memo[i][curr_capacity]
        
        memo = [[-1] * (capacity + 1) for _ in range(len(profit))]
        return dp(0, capacity, memo)

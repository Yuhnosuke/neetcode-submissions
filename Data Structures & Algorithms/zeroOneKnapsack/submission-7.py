class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit))]

        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[0][c] = weight[0]
        

        for i in range(len(profit)):
            for c in range(capacity + 1):
                # not include
                not_include = dp[i - 1][c]

                # include
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i - 1][c - weight[i]]
                
                dp[i][c] = max(not_include, include)
        
        return dp[-1][-1]
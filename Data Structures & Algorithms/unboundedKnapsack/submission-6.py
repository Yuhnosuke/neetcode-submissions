class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity + 1) for _ in range(len(profit))]
        for c in range(capacity + 1):
            if c >= weight[0]:
                dp[0][c] = profit[0]
        
        for p in range(len(profit)):
            for c in range(capacity + 1):
                # skip
                dp[p][c] = dp[p - 1][c]
                # take
                if c - weight[p] >= 0:
                    dp[p][c] = max(profit[p] + dp[p][c - weight[p]], dp[p][c])
        
        return dp[len(profit) - 1][capacity]

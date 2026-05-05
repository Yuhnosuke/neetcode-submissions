class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        rows = len(profit)
        columns = capacity + 1

        dp = [[0] * columns for _ in range(rows)]

        for r in range(rows):
            dp[r][0] = 0

        for c in range(1, columns):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for r in range(1, rows):
            for c in range(1, columns):
                skip = dp[r - 1][c]
                take = 0
                if c - weight[r] >= 0:
                    take = profit[r] + dp[r - 1][c - weight[r]]
                dp[r][c] = max(skip, take)
        
        return dp[rows - 1][columns - 1]
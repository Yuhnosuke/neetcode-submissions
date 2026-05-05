class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        rows = len(profit)
        columns = capacity + 1

        dp = [[0] * columns for _ in range(rows)]
        for r in range(rows):
            dp[r][0] = 0
        for c in range(columns):
            if weight[0] <= c:
                dp[0][c] = (c // weight[0]) * profit[0]
        
        for i in range(1, rows):
            for c in range(1, columns):
                skip = dp[i - 1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i][c - weight[i]]
                dp[i][c] = max(include, skip)
        return dp[rows - 1][columns - 1]

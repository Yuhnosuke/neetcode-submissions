class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(i: int, j: int) -> int:
            if i == m - 1 or j == n - 1:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]

            answer = dp(i + 1, j) + dp(i, j + 1)
            
            memo[(i, j)] = answer
            return answer


        memo = {}
        return dp(0, 0)
        
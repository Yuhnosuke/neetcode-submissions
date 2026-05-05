class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]

            answer = dp(i - 1, j) + dp(i, j - 1)
            
            memo[(i, j)] = answer
            return answer


        memo = {}
        return dp(m - 1, n - 1)
        
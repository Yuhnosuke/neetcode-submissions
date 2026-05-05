class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i: int) -> int:
            if i == 1:
                return 1
            if i == 2:
                return 1
            
            if i in memo:
                return memo[i]
            
            memo[i] = dp(i - 2) + dp(i - 1)

            return memo[i]
        
        memo = {}
        return dp(n + 1)
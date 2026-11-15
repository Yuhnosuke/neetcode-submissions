class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(curr: int) -> int:
            if curr == 0:
                return 0
            if curr < 0:
                return float("inf")
            if curr in memo:
                return memo[curr]

            memo[curr] = min([1 + dp(curr - coin) for coin in coins])
            return memo[curr]
        
        memo = {}
        res = dp(amount)
        return res if res != float("inf") else -1
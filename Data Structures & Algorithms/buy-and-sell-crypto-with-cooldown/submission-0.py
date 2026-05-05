class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i: int, is_buying: bool):
            
            if i >= len(prices):
                return 0

            if (i, is_buying) in memo:
                return memo[(i, is_buying)]
            
            cooldown = dfs(i + 1, is_buying)

            if is_buying:
                buy = dfs(i + 1, not is_buying) - prices[i]
                memo[(i, is_buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not is_buying) + prices[i]
                memo[(i, is_buying)] = max(sell, cooldown)

            return memo[(i, is_buying)]
                
        
        memo = {}
        return dfs(0, True)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            while r < len(prices) and prices[r] > prices[l]:
                ans = max(ans, prices[r] - prices[l])
                r += 1

        return ans
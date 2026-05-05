class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])
        
        return min_coins[amount] if min_coins[amount] != amount + 1 else -1
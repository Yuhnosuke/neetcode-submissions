class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = max(piles)
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2

            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / m)

            if time_taken <= h:
                ans = min(ans, m)
                r = m 
            else:
                l = m + 1

        return ans
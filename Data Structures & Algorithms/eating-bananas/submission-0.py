class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
            
            if hours <= h:
                answer = min(answer, k)
                right = k - 1
            else:
                left = k + 1
        
        return answer
        
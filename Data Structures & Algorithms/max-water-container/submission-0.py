class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        answer = float("-INF")

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            current_max = h * w
            answer = max(answer, current_max)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

        return answer
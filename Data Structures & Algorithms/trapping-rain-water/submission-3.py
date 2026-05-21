class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        for i in range(len(height)):
            # left_highest
            left_highest = 0
            for l in range(0, i):
                left_highest = max(left_highest, height[l])
            # right_highest
            right_highest = 0
            for r in range(i + 1, len(height)):
                right_highest = max(right_highest, height[r])
            
            bottle_neck = min(left_highest, right_highest)
            ans += max(bottle_neck - height[i], 0)
        return ans


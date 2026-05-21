class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_highest, right_highest = height[l], height[r]
        ans = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                left_highest = max(left_highest, height[l])
                ans += left_highest - height[l]
            else:
                r -= 1
                right_highest = max(right_highest, height[r])
                ans += right_highest - height[r]
        return ans

        
        
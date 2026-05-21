class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        for i, curr_height in enumerate(height):
            left_highest = float("-inf")
            for l in range(0, i):
                left_highest = max(left_highest, height[l])
            
            right_highest = float("-inf")
            for r in range(i + 1, len(height)):
                right_highest = max(right_highest, height[r])
            
            ans += max(min(left_highest, right_highest) - curr_height, 0)
        return ans

 



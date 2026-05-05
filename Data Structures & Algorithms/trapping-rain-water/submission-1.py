class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        ans = 0

        while l < r:
            if left_max < right_max:
                l += 1
                curr_height = height[l]
                if curr_height >= left_max:
                    left_max = curr_height
                ans += left_max - curr_height
            else:
                r -= 1
                curr_height = height[r]
                if curr_height >= right_max:
                    right_max = curr_height
                ans += right_max - curr_height

        return ans
        
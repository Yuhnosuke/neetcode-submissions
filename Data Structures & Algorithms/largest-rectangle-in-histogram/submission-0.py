class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            l, r = i, i
            curr_height = heights[i]

            while l > 0 and heights[l - 1] >= curr_height:
                l -= 1
            while r < len(heights) - 1 and heights[r + 1] >= curr_height:
                r += 1
            width = r - l + 1        
            ans = max(ans, curr_height * width)
            
        return ans
        
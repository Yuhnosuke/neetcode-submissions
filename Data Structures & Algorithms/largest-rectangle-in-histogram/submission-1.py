class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        prev_heights = [] # (index, height)

        for curr_i, curr_h in enumerate(heights):
            s = curr_i # for Tunneling
            while prev_heights and prev_heights[-1][1] > curr_h:
                prev_i, prev_h = prev_heights.pop()
                max_area = max(max_area, prev_h * (curr_i - prev_i))
                s = prev_i
            prev_heights.append((s, curr_h))
        
        for prev_i, prev_h in prev_heights:
            max_area = max(max_area, prev_h * (len(heights) - prev_i))

        return max_area
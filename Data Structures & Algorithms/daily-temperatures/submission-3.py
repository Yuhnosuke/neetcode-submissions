class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # (temp, index)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append((temp, i))
        return ans

 
            
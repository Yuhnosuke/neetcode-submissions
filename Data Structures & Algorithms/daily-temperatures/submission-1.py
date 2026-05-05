class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        past_temp_idxs = []
        ans = [0] * len(temperatures)

        for c in range(len(temperatures)):
            curr_temp = temperatures[c]
            while past_temp_idxs and temperatures[past_temp_idxs[-1]] < curr_temp:
                p = past_temp_idxs.pop()
                ans[p] = c - p
            past_temp_idxs.append(c)


        return ans
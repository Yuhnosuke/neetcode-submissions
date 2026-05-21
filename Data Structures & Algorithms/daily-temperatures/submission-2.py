class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temp:
                    ans[i] = j - i
                    break
        return ans

 
            
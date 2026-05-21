class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        past_days = [] # (temp, idx)

        for i, temp in enumerate(temperatures):
            while past_days and temp > past_days[-1][0]:
                past_temp, past_idx = past_days.pop()
                answer[past_idx] = i - past_idx
            past_days.append((temp, i))
        
        return answer

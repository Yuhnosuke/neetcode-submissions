from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        
        frequency_array = []
        for key, value in frequency_map.items():
            frequency_array.append([value, key])
        frequency_array.sort()
        
        answer = []
        while len(answer) < k:
            popped = frequency_array.pop()
            answer.append(popped[1])
        
        return answer

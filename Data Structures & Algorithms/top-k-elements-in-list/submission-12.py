class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for num in nums:
            num_to_freq[num] = 1 + num_to_freq.get(num, 0)
        freq_to_num = [[] for _ in range(len(nums) + 1)] # index: freqency, value: number
        
        for n, f in num_to_freq.items():
            freq_to_num[f].append(n)
        
        answer = []
        for i in range(len(freq_to_num) - 1, 0, -1):
            for num in freq_to_num[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer


        
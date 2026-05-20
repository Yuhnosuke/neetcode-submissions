class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count frequency with hashmap
        # 2. heap
        # 3. bucket sort
        
        num_to_count = {}
        for num in nums:
            num_to_count[num] = 1 + num_to_count.get(num, 0)
        
        count_to_nums = [[] for _ in range(len(nums) + 1)]
        for n, c in num_to_count.items():
            count_to_nums[c].append(n)
        
        ans = []
        for n in range(len(count_to_nums) - 1, 0, -1):
            for num in count_to_nums[n]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        
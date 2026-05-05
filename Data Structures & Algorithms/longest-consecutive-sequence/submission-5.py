import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        ans = 1
        curr_len = 1

        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        curr_num = -heapq.heappop(max_heap)

        while max_heap:
            next_num = -heapq.heappop(max_heap)

            if curr_num - next_num == 0:
                continue

            if curr_num - next_num == 1:
                curr_len += 1
            else:
                curr_len = 1
            
            ans = max(ans, curr_len)
            curr_num = next_num

        return ans

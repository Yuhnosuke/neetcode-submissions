class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        # 2 3 4 5
        # 20
        # 10

        ans = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                curr = 0
                while num + curr in num_set:
                    curr += 1
                ans = max(ans, curr)
        return ans
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            ans = ans ^ nums[i] ^ i

        return ans ^ n
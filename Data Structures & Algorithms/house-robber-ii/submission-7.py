class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(i: int, arr, memo: dict) -> int:

            if i == 0:
                return arr[i]
            if i == 1:
                return max(arr[0], arr[1])
            
            if i in memo:
                return memo[i]

            memo[i] = max(arr[i] + dp(i - 2, arr, memo), dp(i - 1, arr, memo))
            
            return memo[i]
        
        if len(nums) == 1:
            return nums[0]

        with_first = nums[:-1]
        with_last = nums[1:]

        memo_for_first = {}
        memo_for_last = {}

        return max(
            dp(len(with_first) - 1, with_first, memo_for_first),
            dp(len(with_last) - 1, with_last, memo_for_last),
        )
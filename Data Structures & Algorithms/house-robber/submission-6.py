class Solution:
    def rob(self, nums: List[int]) -> int:
        best_before_last, best_so_far = 0, 0
        for amount in nums:
            rob = best_before_last + amount
            skip = best_so_far
            best_before_last = best_so_far
            best_so_far = max(rob, skip)
        return best_so_far

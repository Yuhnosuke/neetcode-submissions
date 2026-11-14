class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back, one_back = 0, 0
        for num in nums:
            max_so_far = max(num + two_back, one_back)
            two_back = one_back
            one_back = max_so_far
        return one_back
 
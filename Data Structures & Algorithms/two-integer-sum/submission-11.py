class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_to_i = {}

        for i, num in enumerate(nums):
            finding = target - num
            if finding in prev_to_i:
                return [prev_to_i[finding], i]
            prev_to_i[num] = i
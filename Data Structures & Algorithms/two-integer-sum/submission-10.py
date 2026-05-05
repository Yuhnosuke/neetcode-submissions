class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            num_to_index[nums[i]] = i
        
        for i in range(len(nums)):
            finding = target - nums[i]
            if finding in num_to_index and num_to_index[finding] != i:
                return [i, num_to_index[finding]]
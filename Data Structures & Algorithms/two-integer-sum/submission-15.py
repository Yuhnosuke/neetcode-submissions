class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key -> num
        # value -> index
        # {
        #     3: 0,
        #     4: 1,
        #     5: 2,
        #     6: 3,
        # }

        # {
        #     5: 1,
        # }
        {

        }
        num_to_idx = defaultdict(int)
        
        for i in range(len(nums)):
            finding = target - nums[i]
            if finding in num_to_idx:
                return [num_to_idx[finding], i]
            num_to_idx[nums[i]] = i
            

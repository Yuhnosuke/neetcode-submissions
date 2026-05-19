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

        num_to_idx = defaultdict(int)
        for idx in range(len(nums)):
            num_to_idx[nums[idx]] = idx
        
        for i in range(len(nums)):
            finding = target - nums[i]
            if finding in num_to_idx and num_to_idx[finding] != i:
                return [i, num_to_idx[finding]]
            

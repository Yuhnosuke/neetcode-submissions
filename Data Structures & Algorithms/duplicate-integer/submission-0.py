from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearance_map = defaultdict(int)
        for i in range(0, len(nums)):
            appearance_map[nums[i]] += 1            
        
        for value in appearance_map.values():
            if value > 1:
                return True
        return False
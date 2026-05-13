class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast]:
                break
        
        slow2 = 0
        while True:
            if nums[slow] == nums[slow2]:
                return nums[slow]
            slow = nums[slow]
            slow2 = nums[slow2]
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(i: int, curr: List[int]) -> None:
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)

            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, curr)

        nums.sort()
        backtrack(0, curr)
        return res

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i: int, curr: List[int]) -> None:
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if sum(curr) > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i, curr)

            curr.pop()
            backtrack(i + 1, curr)
        
        backtrack(0, [])
        return res


            

        
        
        

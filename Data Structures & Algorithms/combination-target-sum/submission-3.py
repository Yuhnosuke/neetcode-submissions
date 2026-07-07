class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i: int, curr: List[int], curr_total) -> None:
            if curr_total == target:
                res.append(curr.copy())
                return
            
            if curr_total > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i, curr, curr_total + nums[i])

            curr.pop()
            backtrack(i + 1, curr, curr_total)
        
        backtrack(0, [], 0)
        return res


            

        
        
        

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def backtrack(i: int, curr: List[int], curr_sum: int) -> None:
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if sum(curr) > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, curr, curr_sum + candidates[i])

            curr.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr, curr_sum)
        
        candidates.sort()
        backtrack(0, curr, 0)
        return res


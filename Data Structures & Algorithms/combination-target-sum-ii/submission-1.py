class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        candidates.sort()
        
        def backtrack(i: int, curr: List[int], curr_sum: int) -> None:            
            if curr_sum == target:
                res.append(curr.copy())
                return
            
            if curr_sum > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            backtrack(i + 1, curr, curr_sum + candidates[i])

            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr, curr_sum)

        backtrack(0, curr, 0)
        return res
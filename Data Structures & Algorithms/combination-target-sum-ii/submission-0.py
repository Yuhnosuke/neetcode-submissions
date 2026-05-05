class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        curr = []

        candidates.sort()

        def backtrack(i: int) -> None:
            if sum(curr) == target:
                answer.append(curr.copy())
                return

            if sum(curr) > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i + 1)

            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1)


        backtrack(0)
        return answer
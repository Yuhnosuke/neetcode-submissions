class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], i: int) -> None:
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(curr, i + 1)

            curr.pop()
            backtrack(curr, i + 1)

        backtrack([], 0)
        return res
        
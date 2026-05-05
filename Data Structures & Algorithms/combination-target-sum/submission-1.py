class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(curr, i, total):
            if total == target:
                answer.append(curr[:])
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return

                curr.append(nums[j])
                backtrack(curr, j, total + nums[j])
                curr.pop()

        answer = []
        nums.sort()
        backtrack([], 0, 0)
        return answer
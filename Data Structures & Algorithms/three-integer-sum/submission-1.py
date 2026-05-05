class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        answer = set()
        nums.sort()

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        answer.add((nums[i], nums[j], nums[k]))
        res = []
        for a in answer:
            res.append(list(a))
        return res
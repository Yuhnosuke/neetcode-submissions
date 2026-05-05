class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        current_min, current_max = 1, 1

        for num in nums:
            if num == 0:
                current_min, current_max = 1, 1
                continue
            
            copied_current_max = current_max
            current_max = max(num * current_max, num * current_min, num)
            current_min = min(num * copied_current_max, num * current_min, num)

            answer = max(answer, current_max)

        return answer
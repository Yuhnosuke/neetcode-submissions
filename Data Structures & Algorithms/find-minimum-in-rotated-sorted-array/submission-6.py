class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        answer = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                answer = min(answer, nums[left])
                break
            
            mid = (left + right) // 2
            answer = min(answer, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
                
            
        return answer
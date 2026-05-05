class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        target = len(nums) - 1
        pointer = target - 1

        answer = False

        while pointer >= 0:
            if pointer + nums[pointer] >= target:
                target = pointer
                pointer -= 1
                answer = True
            else:
                pointer -= 1
                answer = False
        
        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i])
        
        postfix = [nums[-1]]
        p = 0
        for i in range(len(nums) - 2, -1, -1):
            postfix.append(postfix[p] * nums[i])
            p += 1
        
        postfix = postfix[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[i + 1])
            elif i == len(nums) - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(prefix[i - 1] * postfix[i + 1])
        return ans
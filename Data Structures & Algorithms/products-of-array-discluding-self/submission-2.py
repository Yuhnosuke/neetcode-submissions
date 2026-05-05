class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        unit = 1
        pre = []
        for i in range(len(nums)):
            if i == 0:
                pre.append(nums[i] * unit)
            else:
                pre.append(nums[i] * pre[-1])
        
        post = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) -1:
                post.append(nums[i] * unit)
            else:
                post.append(nums[i] * post[-1])
        
        post = post[::-1]
        
        ans = []
        
        for i in range(len(nums)):
            if i == 0:
                ans.append(post[1])
            elif i == len(nums) - 1:
                ans.append(pre[-2])
            else:
                ans.append(pre[i - 1] * post[i + 1])
        
        return ans

            

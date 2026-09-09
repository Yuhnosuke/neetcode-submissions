class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []

        pre_product = 1
        for num in nums:
            pre_product *= num
            pre.append(pre_product)
        
        suf_product = 1
        for i in range(len(nums) - 1, -1, -1):
            suf_product *= nums[i]
            suf.append(suf_product)
        suf = suf[::-1]

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(suf[i + 1])
            elif i == len(nums) - 1:
                output.append(pre[i - 1])
            else:
                output.append(pre[i - 1] * suf[i + 1])
        return output

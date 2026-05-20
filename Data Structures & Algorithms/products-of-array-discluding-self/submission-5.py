class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [nums[0]]
        for i in range(1, len(nums)):
            prefix_product.append(prefix_product[-1] * nums[i])
        
        suffix_product = [nums[-1]]
        for i in range(len(nums) -2, -1, -1):
            suffix_product.append(suffix_product[-1] * nums[i])
        suffix_product.reverse()

        ans = [1] * len(nums)
        for i in range(len(ans)):
            if i == 0:
                ans[i] = suffix_product[i + 1]
            elif i == len(ans) - 1:
                ans[i] = prefix_product[i - 1]
            else:
                ans[i] = prefix_product[i - 1] * suffix_product[i + 1]
        return ans


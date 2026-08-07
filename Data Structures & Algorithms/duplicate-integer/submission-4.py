class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        def is_seen(num):
            return num in seens
            
        seens = set()

        for num in nums:
            if is_seen(num):
                return True
            seens.add(num)
        return False


        
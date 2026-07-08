class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []

        num_to_count = defaultdict(int)
        for num in nums:
            num_to_count[num] += 1

        def backtrack() -> None:
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in num_to_count:
                if num_to_count[num] <= 0:
                    continue
                
                curr.append(num)
                num_to_count[num] -= 1

                backtrack()

                curr.pop()
                num_to_count[num] += 1

        backtrack()
        return res
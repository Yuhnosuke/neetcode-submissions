from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = defaultdict(list)

        for i in range(0, len(nums)):
            index_map[nums[i]].append(i)

        for i in range(0, len(nums)):
            finding = target - nums[i]
            if finding in index_map and index_map[finding][0] != i:
                x = index_map.get(finding)
                if len(x) == 2:
                    return [x[0], x[1]]
                else:
                    return [i, x[0]]
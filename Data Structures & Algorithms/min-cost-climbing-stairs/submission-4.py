class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        one_prev, two_prev = 0, 0

        for i in range(2, len(cost) + 1):
            two_prev, one_prev = one_prev, min(cost[i - 1] + one_prev, cost[i - 2] + two_prev)

        return one_prev


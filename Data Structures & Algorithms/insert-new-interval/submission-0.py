class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # newIntervalが完全に左になるケース
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newIntervalが完全に右になるケース
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # 重なるケース
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        res.append(newInterval)

        return res

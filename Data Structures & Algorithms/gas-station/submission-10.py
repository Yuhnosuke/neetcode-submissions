class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1

        diffs = []
        for g, c in zip(gas, cost):
            diffs.append(g - c)
        
        profit_indices = []
        for i in range(len(diffs)):
            if diffs[i] > 0:
                profit_indices.append(i)
        
        if len(profit_indices) == 0:
            return -1
        
        answer = None
        
        for profit_index in profit_indices:
            tank = 0
            for i in range(len(diffs) + 1):
                tank += diffs[(profit_index + i) % len(diffs)]

                if tank < 0:
                    break
                
            if tank >= 0:
              answer = profit_index
        return answer if answer != None else -1
        


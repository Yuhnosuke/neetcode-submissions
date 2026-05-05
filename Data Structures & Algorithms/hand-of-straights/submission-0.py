from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        value_frequency_map = defaultdict(int)
        for value in hand:
            value_frequency_map[value] += 1

        sorted_values = sorted(value_frequency_map)

        for value in sorted_values:
            if value_frequency_map[value] > 0:
                frequency = value_frequency_map[value]
                for i in range(groupSize):
                    if value_frequency_map[value + i] < frequency:
                        return False
                    value_frequency_map[value + i] -= frequency
        
        return True
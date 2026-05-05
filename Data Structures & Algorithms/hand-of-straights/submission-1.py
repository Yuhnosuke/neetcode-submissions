from collections import defaultdict
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        value_frequency_map = defaultdict(int)
        for value in hand:
            value_frequency_map[value] += 1
        
        min_heap = list(value_frequency_map.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in value_frequency_map:
                    return False
                
                value_frequency_map[i] -= 1

                if value_frequency_map[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


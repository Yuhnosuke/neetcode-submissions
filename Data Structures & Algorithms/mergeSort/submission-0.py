# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge_helper(pairs: List[Pair], s, m, e):
            left = pairs[s:m + 1]
            right = pairs[m + 1: e + 1]

            l = 0
            r = 0
            p = s

            while l < len(left) and r < len(right):
                if left[l].key <= right[r].key:
                    pairs[p] = left[l]
                    l += 1
                else:
                    pairs[p] = right[r]
                    r += 1
                p += 1

            while l < len(left):
                pairs[p] = left[l]
                l += 1
                p += 1
            while r < len(right):
                pairs[p] = right[r]
                r += 1
                p += 1


        def merge_sort_helper(pairs: List[Pair], s: int, e: int):

            if e - s + 1 <= 1:
                return pairs

            m = (s + e) // 2

            merge_sort_helper(pairs, s, m)
            merge_sort_helper(pairs, m + 1, e)

            merge_helper(pairs, s, m, e)

            return pairs
        
        return merge_sort_helper(pairs, 0, len(pairs))
        

        

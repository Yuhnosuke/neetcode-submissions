class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first_target = target[0]
        second_target = target[1]
        third_target = target[2]

        for a, b, c in triplets:
            triplet = [a, b, c]
            if a > first_target:
                if triplet in triplets:
                    triplets.remove(triplet)
            if b > second_target:
                if triplet in triplets:
                    triplets.remove(triplet)
            if c > third_target:
                if triplet in triplets:
                    triplets.remove(triplet)

        return first_target in list(map(lambda x: x[0], triplets)) and second_target in list(map(lambda x: x[1], triplets)) and third_target in list(map(lambda x: x[2], triplets))
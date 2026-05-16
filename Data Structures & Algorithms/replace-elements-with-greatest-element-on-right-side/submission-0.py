class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            max_so_far = 0
            for j in range(i + 1, n):
                max_so_far = max(max_so_far, arr[j])
            arr[i] = max_so_far
        
        arr[-1] = -1
        return arr
        



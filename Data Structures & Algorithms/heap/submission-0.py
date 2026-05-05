class MinHeap:
    def __init__(self):
        self.min_heap = [0]

    def push(self, val: int) -> None:
        self.min_heap.append(val)
        self._percolate_up(len(self.min_heap) - 1)

    def pop(self) -> int:
        if len(self.min_heap) < 2:
            return -1
        
        if len(self.min_heap) == 2:
            return self.min_heap.pop()

        root = self.min_heap[1]
        self.min_heap[1] = self.min_heap.pop()
        self._percolate_down(1)

        return root

    def top(self) -> int:
        if len(self.min_heap) < 2:
            return -1
        return self.min_heap[1] 

    def heapify(self, nums: List[int]) -> None:
        self.min_heap = [0] + nums


        for i in range(len(self.min_heap) // 2, 0, -1):
            self._percolate_down(i)

    def _percolate_up(self, index: int) -> None:
        parent = index // 2
        while index > 1 and self.min_heap[parent] > self.min_heap[index]:
            self.min_heap[parent], self.min_heap[index] = (
                self.min_heap[index],
                self.min_heap[parent],
            )
            index = parent
            parent = index // 2

    def _percolate_down(self, index: int) -> None:
        child = 2 * index
        while child < len(self.min_heap):
            if (
                child + 1 < len(self.min_heap)
                and self.min_heap[child] > self.min_heap[child + 1]
            ):
                child += 1

            if self.min_heap[child] >= self.min_heap[index]:
                break

            self.min_heap[child], self.min_heap[index] = (
                self.min_heap[index],
                self.min_heap[child],
            )
            index = child
            child = 2 * index

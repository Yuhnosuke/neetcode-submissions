class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            tmp_min = float("inf")
            for v in self.stack:
                tmp_min = min(tmp_min, v)
            self.min_val = tmp_min

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.min_val
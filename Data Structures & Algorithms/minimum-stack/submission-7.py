class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            curr_min = self.min_stack[-1]
            if val <= curr_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_min)
        else:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        

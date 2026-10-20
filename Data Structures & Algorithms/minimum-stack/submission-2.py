class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minVal:
            self.minVal.append(val)
        else:
            lastMinVal = self.minVal[-1]
            self.minVal.append(min(lastMinVal, val))

    def pop(self) -> None:
        val = self.stack.pop()
        
        self.minVal.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]

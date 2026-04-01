class MinStack:

    def __init__(self):
        self.stack = []
        self.mini_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini_stack and self.mini_stack[-1] > val:
            self.mini_stack.append(val)
        elif self.mini_stack:
            self.mini_stack.append(self.mini_stack[-1])
        else:
            self.mini_stack.append(val)


    def pop(self) -> None:
        self.mini_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_stack[-1] if self.mini_stack else None

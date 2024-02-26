class MinStack:
    def __init__(self):
        self.stack_list = list()
        self.min_stack = list()

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack_list.append(val)

    def pop(self) -> None:
        self.stack_list.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack_list[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

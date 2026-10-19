class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stk=[]

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stk:
            self.min_stk.append(value)
        elif self.min_stk[-1] < value:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
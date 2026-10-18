from collections import deque
class MyStack:

    def __init__(self):
        self.values=deque()

    def push(self, x: int) -> None:
        self.values.append(x)
        # move the prev el behind the new el
        for i in range(len(self.values)-1):
            self.values.append(self.values.popleft())

    def pop(self) -> int:
        if not self.values:
            return 0
        return self.values.popleft()

    def top(self) -> int:
        if not self.values:
            return 0
        return self.values[0]

    def empty(self) -> bool:
        return len(self.values)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""
Topic: Stack
Leetcode: 155. Min Stack
https://leetcode.com/problems/min-stack/
"""

from collections import deque

class MinStack:

    def __init__(self):
        self.st = deque()
        

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin is None or val < curMin:
            curMin = val
        self.st.append((val, curMin))
        

    def pop(self) -> None:
        return self.st.pop()
        

    def top(self) -> int:
        if self.st:
            return self.st[-1][0]
        else:
            return None
        

    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



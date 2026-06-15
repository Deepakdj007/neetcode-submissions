from collections import deque
import math

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_ele = math.inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_ele = val

        elif val>=self.min_ele:
            self.stack.append(val)
        
        else:
            self.stack.append(2*val-self.min_ele)
            self.min_ele = val
        

    def pop(self) -> None:
        if not self.stack:
            return

        top_val = self.stack.pop()
        if top_val<self.min_ele:
            self.min_ele = 2*self.min_ele - top_val

    def top(self) -> int:
        if not self.stack:
            return None
        top_val = self.stack[-1]

        return self.min_ele if top_val<self.min_ele else top_val
            

    def getMin(self) -> int:
        return self.min_ele

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        para_map = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = deque()

        for c in s:
            if c in para_map:
                if not stack or stack.pop()!=para_map[c]:
                    return False
            else:
                stack.append(c)
        return not stack

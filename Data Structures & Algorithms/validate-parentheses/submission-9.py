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
            print(para_map.get(c))
            if stack and para_map.get(c) and stack[-1]==para_map[c]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)

        return True if not stack else False

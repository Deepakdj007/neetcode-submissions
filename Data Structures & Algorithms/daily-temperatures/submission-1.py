from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = deque()
        output = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]]<temp:
                    output[temp_stack[-1]] = i-temp_stack[-1]
                    temp_stack.pop()
                    
            temp_stack.append(i)

        return output
                 

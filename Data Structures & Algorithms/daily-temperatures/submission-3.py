class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        output = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]]<temp:
                    index = temp_stack.pop()
                    output[index] = i-index
                    
                    
            temp_stack.append(i)

        return output
                 

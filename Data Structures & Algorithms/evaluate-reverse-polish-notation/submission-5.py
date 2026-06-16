from collections import deque
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        operators_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        operands_stack = deque()

        for ele in tokens:
            if ele not in operators_map:
                operands_stack.append(ele)
            else:
                operand_two = operands_stack.pop()
                operand_one = operands_stack.pop()

                result = operators_map[ele](int(operand_one),int(operand_two))
                operands_stack.append(result)
        
        return int(operands_stack.pop())
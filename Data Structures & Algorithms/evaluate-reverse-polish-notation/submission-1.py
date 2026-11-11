from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque() 
        op = {
            '+' : lambda a, b: a + b,
            '-' : lambda a, b: a - b,
            '*' : lambda a, b: a * b,
            '/' : lambda a, b: int(a / b)
        }  
 

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(str(op[token](num2, num1)))
            else:
                stack.append(token)
            
        ans = int(stack[-1])

        return ans


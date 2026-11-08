from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        stack.append("$")
        for char in s:
            top = stack[-1] if stack else None
            
            if (
                top == "(" and char == ")" or
                top == "{" and char == "}" or
                top == "[" and char == "]"
            ):
                stack.pop()
            else:
                stack.append(char)
        
        if stack[-1] == "$":
            return True
        else:
            return False
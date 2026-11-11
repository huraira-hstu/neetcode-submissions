from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        area = 0
        left = 0
        
        heights.append(0)
        
        for i, height in enumerate(heights):
            if not stack or (stack and height > stack[-1][0]):
                stack.append([height, i])  
            else:
                while stack and height <= stack[-1][0]:
                    h, left = stack.pop()
                    area = max(area, h * (i - left))
                stack.append([height, left])
            
        return area
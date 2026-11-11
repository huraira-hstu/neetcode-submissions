
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        ans = [0] * n 
        stack = []
        for i, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                _, pos = stack.pop()
                ans[pos] = i - pos
            stack.append([temp, i])
        return ans



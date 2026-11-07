class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        
        ans = 0
        maxl, maxr = 0, 0

        while l < r:
            trapped = 0
            maxl, maxr = max(height[l], maxl), max(height[r], maxr)
            if height[l] < height[r]:
                trapped = max(0, min(maxr, maxl) - height[l + 1])
                l += 1
            else:
                trapped = max(0, min(maxr, maxl) - height[r - 1])
                r -= 1
            ans += trapped
        return ans
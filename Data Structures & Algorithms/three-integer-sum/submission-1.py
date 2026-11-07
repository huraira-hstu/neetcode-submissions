class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        solve = [] 
        match = {}
        
        for i, a in enumerate(nums):
            seen = {}
            for j in range(i + 1, len(nums)):
                b = nums[j]
                c = -(a+b)
                if c in seen:
                    x, y, z = sorted([a,b,c]) 
                    if not(x in match and y in match[x]):
                        solve.append([x, y, z])
                        if x in match:
                            match[x][y] = True
                        else:
                            match[x] = {y:True}
                else:
                    seen[b] = True
        
        return solve



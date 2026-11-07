class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        prod = 1
        sol = []
        
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                prod *= num
        

        if zeroCount > 1:
            return [0 for _ in range(len(nums))]
        elif zeroCount == 1:
            for num in nums:
                if num == 0:
                    sol.append(prod)
                else:
                    sol.append(0)
        else:
            for num in nums:
                sol.append(prod//num)
        return sol
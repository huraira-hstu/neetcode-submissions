class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        j = 0
    
        for i in range(n):
            nums[j] = nums[i]
            if nums[i] != val:
                j = j + 1
           
        nums = nums[:j]
        return j

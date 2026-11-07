class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0    

        for i, num in enumerate(nums):
            if count == 0:
                candidate = num
                count = count + 1
            else:
                if nums[i] == candidate:
                    count += 1
                else:
                    count -= 1
        
        return candidate
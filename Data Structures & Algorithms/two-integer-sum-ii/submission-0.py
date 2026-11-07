class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            df = nums[left] + nums[right] - target
            if df == 0:
                return [left+1, right+1]
            elif df > 0:
                right -= 1
            else:
                left += 1

        return []
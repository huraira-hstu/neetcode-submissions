
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                cur = num
                cnt = 1
                while (cur + 1) in numset:
                    cnt += 1
                    cur += 1
                longest = max(longest, cnt)
        
        return longest
        
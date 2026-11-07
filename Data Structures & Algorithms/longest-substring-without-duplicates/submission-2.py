 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        charSet = set()
        for r, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(char)
            ans = max(ans, r - l + 1)
        return ans

                
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charCount1 = Counter(s)
        charCount2 = Counter(t)

        for char, freq in charCount1.items():
            if char not in charCount2 or freq != charCount2[char]:
                return False
        return True
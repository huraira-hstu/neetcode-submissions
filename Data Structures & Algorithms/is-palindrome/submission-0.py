class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        n = len(cleaned)
        for i in range(n):
            if cleaned[i] != cleaned[n - 1 - i]:
                return False
        
        return True
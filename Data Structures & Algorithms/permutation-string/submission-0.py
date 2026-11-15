class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        n = len(s2)
        m = len(s1)

        if m > n:
            return False

        def matched() -> bool:
            for i in range(26):
                if count1[i] != count2[i]:
                    return False
            return True

        for i in range(m):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        

        if matched():
            return True

        for i in range(m, n):
            count2[ord(s2[i]) - ord('a')] += 1
            count2[ord(s2[i - m]) - ord('a')] -= 1
            if matched():
                return True
        
        return False

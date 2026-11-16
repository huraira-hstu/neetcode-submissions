class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        matched = 0

        n = len(s2)
        m = len(s1)

        if m > n:
            return False
 

        for i in range(m):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
         
        for i in range(26):
            matched += (1 if count1[i] == count2[i] else 0)
 
        for i in range(m, n):
            if matched == 26:
                return True
            index = ord(s2[i]) - ord('a')
            count2[index] += 1
             
            if count2[index] == count1[index]:
                matched += 1
            elif count2[index] - 1 == count1[index]:
                matched -= 1
            
            index = ord(s2[i - m]) - ord('a')
            count2[index] -= 1
             
            if count2[index] == count1[index]:
                matched += 1
            elif count2[index] + 1 == count1[index]:
                matched -= 1
            
        return matched == 26

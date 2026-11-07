

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs)
       
        for i in range(n):
            for char in strs[i]:
                if char == ',' or char == '/':
                    ans += '/'
                ans += char
            ans += ','
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        cur = ""
        i = 0
        while i < n:
            if s[i] == '/':
                i += 1
                cur += s[i]
            elif s[i] == ',':
                ans.append(cur)
                cur = ""
            else:
                cur += s[i]
            i += 1
        return ans
            
class Solution:
    def longestCommonPrefixLen(self, strs: List[str]) -> int:
        n = len(strs)
        cnt = 0;

        for i in range(len(strs[0])):
            for j in range(1, n):
                if cnt + 1> len(strs[j]):
                    return cnt

                if strs[j][cnt] != strs[0][cnt]:
                    return cnt
        
            cnt = cnt + 1
        
        return cnt

    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = self.longestCommonPrefixLen(strs)
        return strs[0][:n]

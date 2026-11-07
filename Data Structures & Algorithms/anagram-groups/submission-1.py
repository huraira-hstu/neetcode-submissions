from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        ans = []

        for i, string in enumerate(strs):
            groups["".join(sorted(string))].append(string)
        
        for key, val in groups.items():
            ans.append(val)
        
        return ans

            
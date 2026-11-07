from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        ans = []
        for num, cnt in freq.items():
            heapq.heappush(heap, (-cnt, num))
        
        for i in range(k):
            cnt, num = heapq.heappop(heap)
            ans.append(num)
        return ans


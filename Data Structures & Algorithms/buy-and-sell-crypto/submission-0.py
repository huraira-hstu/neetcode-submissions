class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 1000
        high = 0
        
        profit = 0
        for price in prices:
            if price < low:
                low = price
                high = price
            if price > high:
                high = price
            
            profit = max(profit, high - low)

        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestP = 0
        minP = float('inf')
        for price in prices:
            minP = min(minP, price)
            bestP = max(bestP, price - minP)
            
        return bestP

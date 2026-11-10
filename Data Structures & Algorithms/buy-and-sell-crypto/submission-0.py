class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bestP = 0
        lowest = float('inf')
        for price in prices:
            lowest = min(lowest, price)
            bestP = max(bestP, price - lowest)
        return bestP
# Parts list:
#   Data structures:
#     - two number variables: the lowest price so far and the best profit so far
#   Built-ins and methods:
#     - min(a, b)
#     - max(a, b)
#     - float('inf'): a starting value larger than any price
#   Syntax and patterns:
#     - for price in prices:
#     - subtraction: price - lowest
#     - starting the best profit at 0 handles the no-profit case
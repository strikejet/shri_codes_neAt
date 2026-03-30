class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = False
        profit = 0
        i = 0
        if len(prices) in (0, 1):
            return 0

        while i < len(prices):
            curr = prices[i]
            while i+1<len(prices) and prices[i+1] > prices[i]:
                i = i + 1
            profit= profit + prices[i] - curr
            i = i + 1
        return profit


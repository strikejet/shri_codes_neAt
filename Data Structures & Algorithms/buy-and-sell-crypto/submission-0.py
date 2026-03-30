class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        max_profit = 0
        while right < len(prices) - 1:
            right = right + 1
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[left] >prices[right]:
                left = right
        return max_profit
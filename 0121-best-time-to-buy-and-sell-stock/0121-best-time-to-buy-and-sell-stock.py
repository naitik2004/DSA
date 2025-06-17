class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        min_profit = prices[0]
        for i in range(1, len(prices)):
            if min_profit > prices[i]:
                min_profit = prices[i]
            elif min_profit < prices[i]:
                curr = max(prices[i] - min_profit, curr)
        return curr

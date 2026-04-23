class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0;
        minBuyPrice = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuyPrice)
            minBuyPrice = min(minBuyPrice, sell)

        return maxProfit



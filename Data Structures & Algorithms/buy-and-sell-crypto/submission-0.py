class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for buy in range(0, len(prices) - 1):
            for sell in range(buy, len(prices)):
                if prices[sell] - prices[buy] > maxProfit:
                    maxProfit = prices[sell] - prices[buy]
        
        return maxProfit
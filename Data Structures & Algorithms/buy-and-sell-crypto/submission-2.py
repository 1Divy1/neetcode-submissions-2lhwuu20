class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = buy = sell = 0

        for i in range(len(prices) - 1):
            best = 0
            for j in range(i, len(prices)):
                diff = prices[j] - prices[i]
                if diff > best:
                    best = diff
            if best > profit:
                profit = best

        return profit
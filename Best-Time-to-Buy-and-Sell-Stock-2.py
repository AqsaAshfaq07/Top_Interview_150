class Solution: 
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > 0:
                if profit > max_profit:
                    max_profit = profit
            else:
                min_price = prices[i]
        return max_profit

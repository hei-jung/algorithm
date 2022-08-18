class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0    # 최대 수익
        min_price = prices[0]    # 최저 매수 가격

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i-1])
            max_profit = max(max_profit, prices[i]-min_price)

        return max_profit

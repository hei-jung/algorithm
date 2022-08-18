class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        bought, sold = 0, -prices[0]  # 거래 안 한 상태 / 0번째 날 주식 산 상태
        for i in range(1, n):
            bought = bought if bought > sold + prices[i] - fee else sold + prices[i] - fee
            sold = sold if sold > bought - prices[i] else bought - prices[i]
        return bought

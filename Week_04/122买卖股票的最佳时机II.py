'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/

122. 买卖股票的最佳时机 II

思路：只要后一天比前一天上涨，就买入、卖出


'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit

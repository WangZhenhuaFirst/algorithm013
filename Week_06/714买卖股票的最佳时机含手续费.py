'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

714. 买卖股票的最佳时机含手续费 
k为正无穷，但有手续费

思路：和情况二类似，
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)










'''


def maxProfit(self, prices: List[int], fee: int) -> int:
    '''时空复杂度O(N)'''
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 0
    dp[0][1] = -prices[0] - fee
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
    return dp[n-1][0]


def maxProfit(self, prices: List[int], fee: int) -> int:
    '''空间复杂度O(1)'''
    n = len(prices)
    if n < 2:
        return 0
    dp_i0 = 0
    dp_i1 = -prices[0] - fee
    for i in range(1, n):
        tmp = dp_i0
        dp_i0 = max(dp_i0, dp_i1 + prices[i])
        dp_i1 = max(dp_i1, tmp - prices[i] - fee)
    return dp_i0

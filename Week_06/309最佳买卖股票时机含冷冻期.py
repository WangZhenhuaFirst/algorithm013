'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

309. 最佳买卖股票时机含冷冻期 （谷歌、亚马逊在半年内面试中考过）
k为正无穷，但又冷却时间

思路：
和情况二类似

dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])





'''


def maxProfit(self, prices: List[int]) -> int:
    '''时空复杂度O(N)'''
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * 3 for _ in range(n+1)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i in range(1, n):
        # dp[i][0]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        # dp[i][1]: 手上持有股票的最大收益
        # dp[i][2]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        dp[i][2] = dp[i-1][1] + prices[i]
    return max(dp[n-1][0], dp[n-1][2])


def maxProfit(self, prices: List[int]) -> int:
    '''空间复杂度O(1)'''
    n = len(prices)
    if n < 2:
        return 0
    dp_i_0 = 0
    dp_i_1 = -prices[0]
    dp_pre_0 = 0  # 代表dp[i-2][0]
    for i in range(1, n):
        tmp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
        dp_pre_0 = tmp
    return dp_i_0

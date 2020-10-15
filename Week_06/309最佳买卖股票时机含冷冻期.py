'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

309. 最佳买卖股票时机含冷冻期 （谷歌、亚马逊在半年内面试中考过）
k为正无穷，但有冷却时间

思路：和情况二类似,


dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]) # 关键的不同在i - 2
要想第i天买入股票，第i-1天就不能卖出股票。所以，不仅可以肯定dp[i-1][0]，也可以肯定dp[i-2][0]







'''


def maxProfit(self, prices: List[int]) -> int:
    '''时空复杂度O(N)'''
    n = len(prices)
    if n < 2:
        return 0

    dp = [[0] * 2 for _ in range(n+1)]  # 是n+1,让i-2在i=1时取到 0
    dp[0][0] = 0
    dp[0][1] = -prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[n-1][0]


def maxProfit(self, prices: List[int]) -> int:
    '''空间复杂度O(1)'''
    n = len(prices)
    if n < 2:
        return 0
    dp_i0 = 0
    dp_i1 = -prices[0]
    dp_pre0 = 0  # 代表dp[i-2][0]
    for i in range(1, n):
        tmp = dp_i0
        dp_i0 = max(dp_i0, dp_i1 + prices[i])
        dp_i1 = max(dp_i1, dp_pre0 - prices[i])
        dp_pre0 = tmp
    return dp_i0

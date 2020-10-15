'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

188. 买卖股票的最佳时机IV （谷歌、亚马逊、字节跳动在半年内面试中考过）
k为任意值，是最通用的情况

思路：
一个有收益的交易至少需要两天（在前一天买入，在后一天卖出，前提是买入价格低于卖出价格）。
如果股票价格数组的长度为 n，则有收益的交易的数量最多为 n / 2（整数除法）。
因此 k 的临界值是 n / 2。如果给定的 k 不小于临界值，即 k >= n / 2，
则可以将 k 扩展为正无穷，此时问题等价于情况二。


如果不根据 k 的值进行优化，在 k 的值很大的时候会超出时间限制。





'''


def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    if k >= n / 2:
        res = 0
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                res += diff
        return res

    dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
    for j in range(1, k+1):
        dp[0][j][0] = 0
        dp[0][j][1] = -prices[0]

    for i in range(1, n):
        for j in range(1, k+1):
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
    return dp[n-1][k][0]

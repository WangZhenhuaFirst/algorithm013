'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

123. 买卖股票的最佳时机III （字节跳动在半年内面试中考过）
k = 2

思路：
类似于k=1,只是现在每天不是2个未知变量，而是4个未知变量：
状态转移方程中的k表示的是 已经进行了的交易次数
dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i]) # 买的时候计数交易次数
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
# dp[i-1][0][0] = 0，因为k是从1开始的，k = 0 意味着根本不允许交易，这时利润当然是 0






'''


def maxProfit(self, prices: List[int]) -> int:
    '''时空复杂度O(N)'''
    n = len(prices)
    if n < 2:
        return 0
    # 为了使得第 2 维的数值 1 和 2 有意义，这里将第 2 维的长度设置为 3，因为这样数组下标1和2才能取到值
    # 这只是为了减小理解负担
    dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]

    dp[0][1][0] = 0  # k=1，即至今最多进行了一次交易
    dp[0][1][1] = -prices[0]
    dp[0][2][0] = 0
    dp[0][2][1] = -prices[0]

    for i in range(1, n):
        dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1]
                          [0] - prices[i])  # 注意，至今最多进行的交易次数有变化
        dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
    return max(dp[n-1][1][0], dp[n-1][2][0], 0)


def maxProfit(self, prices: List[int]) -> int:
    '''
    O(1),因为第i天之和第i-1天相关
    '''
    n = len(prices)
    if n < 2:
        return 0
    dp_i10 = 0
    dp_i11 = -prices[0]
    dp_i20 = 0
    dp_i21 = -prices[0]
    for i in range(1, n):
        dp_i20 = max(dp_i20, dp_i21 + prices[i])
        dp_i21 = max(dp_i21, dp_i10 - prices[i])
        dp_i10 = max(dp_i10, dp_i11 + prices[i])
        dp_i11 = max(dp_i11, -prices[i])
    return max(dp_i20, dp_i10, 0)


def maxProfit(self, prices: List[int]) -> int:
    '''
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    '''
    n = len(prices)
    if n < 2:
        return 0
    max_k = 2
    dp = [[0] * 2 for _ in range(max_k + 1) for _ in range(n+1)]
    for i in range(n):
        for k in (max_k, 0, -1):
            if i - 1 == -1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    return dp[n-1][max_k][0]

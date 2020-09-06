'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/

122. 买卖股票的最佳时机II （亚马逊、字节跳动、微软在半年内面试中考过）
k 为正无穷


思路：
1.只要后一天比前一天上涨，就买入、卖出

2.可以无限次交易，则k 和 k-1 实际上没有任何区别。理解了贪心算法，就容易理解这一点了。
多次交易等价于一次交易，因此k-1次交易和k次交易等价。这是因为只有1股买进卖出。这意味着：
dp[i-1][k-1][0] = dp[i-1][k][0]
dp[i-1][k-1][1] = dp[i-1][k][1]


dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
dp table 中的k不会改变了，也就是说不需要记录k这个状态了。
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])



'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        '''时空复杂度O(N)'''
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

    def maxProfit(self, prices: List[int]) -> int:
        '''
        空间复杂度O(1)
        
        贪心策略:可能的情况下，在每个局部最小值买入股票，然后在之后遇到的第一个局部最大值卖出。
        这等价于找到股票价格数组中的递增子数组，对于每个递增子数组，在开始位置买入并在结束位置卖出
        '''
        n = len(prices)
        if n < 2:
            return 0
        profit0 = 0
        profit1 = -prices[0]
        for i in range(1, n):
            tmp = profit0
            profit0 = max(profit0, profit1 + prices[i])
            profit1 = max(profit1, tmp - prices[i])
        return profit0

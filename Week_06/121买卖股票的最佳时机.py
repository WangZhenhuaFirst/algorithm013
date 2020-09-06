'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/#/description

121. 买卖股票的最佳时机 （亚马逊、字节跳动、Facebook 在半年内面试中常考）

思路：
[一个方法团灭 6 道股票问题](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/)

https://leetcode-cn.com/circle/article/qiAgHn/

具体到每一天，看总共有几种可能的状态，再找出每种状态对应的选择，然后根据对应的选择更新状态。
状态有3个：天数/第几天、允许交易的最大次数、当前的持有状态(这是个需要挖掘的隐含状态，就像打家劫舍问题中每间房子偷/不偷)


k表示允许交易的最多次数。状态转移的思想是：交易k次可以从交易k-1次的结果转换而来，k次的结果包含了k-1次的结果


如果可以将dp[i][k] 关联到子问题，比如dp[i-1][k]、dp[i][k-1]、dp[i-1][k-1] 等，就能得到状态转移方程。
如何得到状态转移方程呢？最直接的办法就是看第i天可能的操作：买入、卖出、无操作
应该选择哪个操作？并不知道。但可以通过计算得到选择每个操作可以得到的最大收益。
假设没有别的条件限制，则可以尝试每一种操作，并选择可以最大化收益的一种操作。
但有限制：不允许同时进行多次交易，这意味着：
如果我们决定在第i天购买股票，那我们手中应该持有0个股票；
如果我们决定在第i天卖出股票，那我们手中应该恰好有1个股票。
因此对dp[i][k]的定义需要分成两项：
dp[i][k][0]表示第i天结束时，最多进行k笔交易且交易完成后，我们当前不持股，而获得的利润；
dp[i][k][1]表示第i天结束时，最多进行k笔交易且交易完成后，我们当前持股，而获得的利润。

base case：
dp[-1][k][0] = 0
dp[-1][k][1] = -infinite # 没有进行股票交易时，不允许持有股票
# 还没发生的交易初始化时应该初始化为负无穷，因为需要比较的是最大值，如果初始化为0，状态转移时会出错

dp[i][0][0] = 0 # k=0意味着根本不允许/没有过交易，这时候利润当然是0
dp[i][0][1] = -infinite


dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][0]中[0]表示不持股，因此第i天采取的操作只能是 休息 或 卖出
如果第i天什么都没做，dp[i-1][k][0]就是最大利润，
如果第i天卖出了股票，dp[i-1][k][1] + prices[i] 是最大利润。
注意：由于交易包含两个成对出现的操作（买入、卖出），因此这个方程中 允许交易的最大数量k保持不变，
只有 购买股票 会影响 允许的最大交易数。

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
dp[i][k][1]表示在第i天 什么都没做 或 买入股票。
如果第i天什么都没做，dp[i-1][k][1] 是最大利润；
如果第i天买入股票，dp[i-1][k-1][0] - prices[i] 是当前最大利润。
注意 运行的最大交易次数 减少了一次，因为每次买入操作会使用一次交易

我们想求的最终答案是：dp[n-1][K][0]，因为结束时持有0份股票的收益一定大于持有1份股票的收益。


我们将6个股票问题按照k的值进行分类。

k = 1
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
            = max(dp[i-1][1][1], -prices[i])





'''


def maxProfit(k: int, prices: List[int]) -> int:
    '''时间、空间复杂度为O(N)'''
    n = len(prices)
    if n < 2:
        return 0
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n-1][0]


def maxProfit(k: int, prices: List[int]) -> int:
    '''空间复杂度O(1)'''
    n = len(prices)
    if n < 2:
        return 0
    profit0 = 0
    profit1 = -prices[0]
    for i in range(1, n):
        profit0 = max(profit0, profit1 + prices[i])
        profit1 = max(profit1, -prices[i])
    return profit0

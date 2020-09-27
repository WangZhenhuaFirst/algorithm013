'''
https://leetcode-cn.com/problems/min-cost-climbing-stairs/

746. 使用最小花费爬楼梯 （亚马逊在半年内面试中考过）

思路：
这道题的难点在于题意不好理解：
1.楼顶在数组之外，所以最后一个元素的体力值也要算上，这就是为什么第二个样例结果是6而不是5
2.踏上第i级台阶花费cost[i],但一大步跨过则不用花费












'''


def minCostClimbingStairs(self, cost: List[int]) -> int:
    '''
    状态dp[i]表示 爬到索为i的位置 再向上爬一步 需要的体力
    状态转移方程：dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    '''
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]  # 肯定是异步跨到索引1花费少；而不是先走到0，再走到1
    for i in range(2, n):
        dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
    return min(dp[-1], dp[-2])  # 要走到楼顶，有两种可能


def minCostClimbingStairs(self, cost: List[int]) -> int:
    '''
    优化空间:注意到状态转移方程中只用到了前面的两个记录，
    可以不用一维数组，只用两个变量保存前面的两个记录，这样空间复杂度就是O(1)了。
    '''
    dp0 = cost[0]
    dp1 = cost[1]
    for i in range(2, len(cost)):
        dp = min(dp0, dp1) + cost[i]
        dp0, dp1 = dp1, dp
    return min(dp0, dp1)


def minCostClimbingStairs(self, cost: List[int]) -> int:
    '''
    更进一步，注意到初始值dp[0] = cost[0]，dp[1] = cost[1]，可以直接复用cost数组来代表dp数组。
    '''
    for i in range(2, len(cost)):
        cost[i] = min(cost[i-2], cost[i-1]) + cost[i]
    return min(cost[-2], cost[-1])

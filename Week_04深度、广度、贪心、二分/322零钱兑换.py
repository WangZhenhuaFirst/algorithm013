'''
https://leetcode-cn.com/problems/coin-change/

322. 零钱兑换（亚马逊在半年内面试中常考）

思考：
动态规划问题 最困难的就是 写出暴力解，即状态转移方程。只要写出暴力解，优化方法无非是用 备忘录或DP table。

计算机解决问题 其实没有任何 奇技淫巧，它唯一的办法就是穷举出所有可能性。
算法设计无非是 先思考 如何穷举，然后再追求 如何聪明地穷举。

列出状态转移方程，就是在解决 如何穷举的问题。之所以说它难，一是因为很多穷举需要递归实现，二是因为有的问题
本身的解空间复杂，不那么容易穷举完整。
备忘录、DP table就是在追求如何聪明地穷举。用空间换时间 的思路，是降低时间复杂度的不二法门，除此之外，还有什么呢？

思路：
1.暴力递归：指数级复杂度
2.BFS:画出递归树，然后做广度优先遍历，直到第一次碰到为0的节点，此时的深度就是答案
3.DP：
coins = [1, 2, 5], amount = 11
凑成面值为11的最小硬币数，可以由以下三者中的最小值得到：
凑成面值为10的最小数 + 面值为1的这一枚
凑成面值为9的最小数 + 面值为2的这一枚
凑成面值为6的最小数 + 面值为5的这一枚
dp[11] = min(dp[10] + 1, dp[9] + 1, dp[6] + 1)
dp[amount] = min(1 + dp[amount - coin[i]]) for i in [0, len - 1] if coin[i] <= amount

这个问题其实和爬楼梯问题、斐波那契数列问题类似，每次走1步、2步、5步 ？
f(n) = f(n-1) + f(n-2)
f(n) = min(f(n - k) for k in [1, 2, 5]) + 1

'''


def coinChange(coins: List[int], amount: int) -> int:
    '''暴力递归'''
    def dp(amount):
        # 递归终止条件
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        res = float('inf')
        for coin in coins:
            subproblem = dp(amount - coin)
            if subproblem == -1:  # 即 amount - coin < 0 时
                continue
            res = min(res, 1 + subproblem)
        return res if res != float('inf') else -1
    return dp(amount)


def coinChange(coins: List[int], amount: int) -> int:
    '''带备忘录的递归'''
    def dp(amount):
        # 先查备忘录，防止重复计算
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        res = float('inf')
        for coin in coins:
            subproblem = dp(amount - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)

        # 每一层递归都要先将结果存到memo中，再return
        memo[amount] = res if res != float('inf') else -1
        return memo[amount]
    memo = dict()
    return dp(amount)


def coinChange(coins: List[int], amount: int) -> int:
    '''动态规划'''
    dp = [float('inf')] * (amount + 1)  # 0到amount，共 amount + 1 个
    dp[0] = 0  # 如果amount为0，那肯定只需要0个硬币了
    # 之所以要从1开始循环i，是因为要先求出小的amount需要的最少硬币数
    # 才能求出 大的amount 需要的最少硬币数
    for i in range(1, amount+1):
        for coin in coins:
            # 每一步都遍历各个硬币种类，当然是 使用最大且<=i的硬币 时用的硬币数最少了
            # 也就是说，状态转移方程中，每种硬币金额都要进去试试
            if coin <= i:  # 如果coin > i，直接 continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # 比如 coins = [2] ，amount = 3 时，i = 1 时，coin > i，导致dp[i] = float('inf')
    # i = 3 时，dp[3] = min(dp[3], dp[1] + 1) = float('inf')
    # 也就是说 amount = 3，coins = [2] 时，- 2 这唯一的一种可能后，剩下的1 是没有硬币能用的
    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]

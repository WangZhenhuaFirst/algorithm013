'''
https://leetcode-cn.com/problems/coin-change-2/

518.零钱兑换II （亚马逊、字节跳动在半年内面试中考过）

思路：完全背包问题，每个硬币 选或不选，
dp[i][j]表示 使用前i种硬币 组成j金额的组合数
dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
就是选和不选两种情况相加，注意选i时的下标仍是i，因为硬币个数无限










'''


def change(self, amount: int, coins: List[int]) -> int:
    '''动态规划'''
    n = len(coins)
    if n == 0:
        if amount == 0:
            return 1
        return 0
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    # for j in range(1, amount + 1):
    #     dp[0][j] = 0  # 没有任何一种硬币，不论需要多少金额，都没有对应的方案
    for i in range(n+1):  # 如果金额amount为0，对多少种硬币来说都是1种方案
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i-1][j]  # 不选当前硬币
            if j - coins[i-1] >= 0:  # coins[i-1]代表第i种硬币
                dp[i][j] += dp[i][j - coins[i-1]]  # 选当前硬币，剩余金额为 j- coins[i-1]
    return dp[-1][-1]


def change(self, amount: int, coins: List[int]) -> int:
    '''空间优化'''
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        # 如果amount比coin还小 也就不用看了，维持上一行时的值即可
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    return dp[amount]

'''
https://leetcode-cn.com/problems/frog-jump/

403. 青蛙过河（亚马逊、苹果、字节跳动在半年内面试中考过）

思路：













'''


def canCross(self, stones: List[int]) -> bool:
    '''
    对每个石头向后更新，求当前石头能够向后前进的步伐
    如果跳到了最后一个石头上，表示能够到达，反之不能到达
    '''
    stone_step = {x: set() for x in stones}
    stone_step[stones[0]].add(1)
    for stone in stones:
        for step in stone_step[stone]:
            # 说明这个step 无法达成前进的目的，只能略过
            # 比如第一个石子只能跳1步，跳到第二个石子
            # 则第二个石子可以跳0、1、2步，其中的0步是没意义的
            if step <= 0:
                continue
            if stone + step in stone_step:
                stone_step[stone + step].update({step-1, step, step+1})
        if stone_step[stones[-1]]:
            return True
    return False


def canCross(self, stones: List[int]) -> bool:
    '''动态规划'''
    n = len(stones)
    dp = [[False] * n for _ in range(n)]
    dp[0][1] = True
    for i in range(1, n):  # dp[i][j]表示上一步 步数为j 能否到达i的位置
        for j in range(i):
            diff = stones[i] - stones[j]  # diff 表示两个石头间的距离
            if diff < 0 or diff >= n or not dp[j][diff]:
                continue
            dp[i][diff] = True
            if diff - 1 >= 0:
                dp[i][diff - 1] = True
            if diff + 1 < n:
                dp[i][diff + 1] = True
    return any(dp[-1])

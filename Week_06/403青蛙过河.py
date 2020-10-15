'''
https://leetcode-cn.com/problems/frog-jump/

403. 青蛙过河（亚马逊、苹果、字节跳动在半年内面试中考过）

思路：



'''


def canCross(self, stones: List[int]) -> bool:
    n = len(stones)
    dp = [[False] * n for _ in range(n)]
    dp[0][1] = True
    for i in range(1, n):
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

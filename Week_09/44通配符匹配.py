'''
https://leetcode-cn.com/problems/wildcard-matching/

44. 通配符匹配 （Facebook、微软、字节跳动在半年内面试中考过）

思路：求两个字符串之间的某种关系的题目，一般都要用动态规划















'''


def isMatch(self, s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    # s 为空串，p要想匹配，只能是 p[j-1] 是 * ，* 匹配 空字符
    for j in range(1, len(p) + 1):
        dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # 星号匹配 >=1个字符，或星号匹配0个字符
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[-1][-1]

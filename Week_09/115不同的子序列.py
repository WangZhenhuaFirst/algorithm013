'''
https://leetcode-cn.com/problems/distinct-subsequences/

115. 不同的子序列 （MathWorks 在半年内面试中考过）

思路：
dp[i][j] 表示 s 的前i个字符 的 子序列中，包含多少个 t 的前j个 字符子串
https://leetcode-cn.com/problems/distinct-subsequences/solution/dong-tai-gui-hua-si-yao-su-by-a380922457-2/




'''


def numDistinct(self, s: str, t: str) -> int:
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    # t为空串时，所有字符串都包含1个空串子集
    for i in range(len(s) + 1):
        dp[i][0] = 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[-1][-1]

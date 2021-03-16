'''
https://leetcode-cn.com/problems/longest-valid-parentheses/

32. 最长有效括号（字节跳动、亚马逊、微软在半年内面试中考过）

思路：有最长字眼，是个 最值型题目，可以考虑动态规划。













'''


def longestValidParentheses(self, s: str) -> int:
    '''
    动态规划
    dp[i]表示以s[i]结尾的最长有效括号的长度。
    显然，有效的字串一定以 ')' 结尾，以 '(' 结尾的子串对应的 dp 值 必定为0
    '''
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * n
    for i in range(n):
        # i-dp[i-1]-1是与当前 ‘)’ 对称的位置，dp[i-1]表示以s[i-1]为结尾的最长有效括号的长度
        if i > 0 and s[i] == ')':
            if s[i-1] == '(':
                dp[i] = 2
                if i - 2 >= 0:
                    dp[i] += dp[i-2]
            elif s[i-1] == ')' and i - dp[i-1] - 1 >= 0 and s[i-dp[i-1] - 1] == '(' and dp[i-1] > 0:
                dp[i] = dp[i-1] + 2
                if i - dp[i-1] - 2 >= 0:
                    dp[i] += dp[i-dp[i-1]-2]
    return max(dp)

'''
https://leetcode-cn.com/problems/palindromic-substrings/

647. 回文子串 （Facebook、苹果、字节跳动在半年内面试中考过）

思路：
正读和反读相同的字符序列为回文，如'aba'、'abba'。
一个长为n的字符串s是回文串的 充要条件是，对于 i ∈ [0, n-1]，都有 s[i] == s[n-1-i]



1.暴力法：嵌套循环，时间复杂度O(N^3)

2.动态规划：
大问题是什么？
规模小一点的问题是什么？剩余字串也是回文串
它们之间有什么联系？

怎么去描述子问题呢？显然，一个字串由两端的i、j指针确定，字串s[i:j]是否是回文串，就是子问题。
'''


def countSubstrings(s: str) -> int:
    '''
    动态规划 O(N^2)
    dp[i][j]表示字串s[i:j]是否是回文串
    '''
    count = 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for j in range(n):
        for i in range(j+1):
            if i == j:  # 只有 1 个字符
                dp[i][j] = 1
                count += 1
            elif j - i == 1 and s[i] == s[j]:  # 有两个字符
                dp[i][j] = 1
                count += 1
            elif j - i > 1 and s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = 1
                count += 1
    return count


def countSubstrings(s: str) -> int:
    '''中心扩展法'''
    self.count = 0

    def helper(i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            self.count += 1
            i -= 1
            j += 1

    for i in range(len(s)):
        helper(i, i)
        helper(i, i+1)
    return self.count

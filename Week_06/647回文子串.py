'''
https://leetcode-cn.com/problems/palindromic-substrings/

647. 回文子串

思路：
正读和反读相同的字符序列为回文，如'aba'、'abba'。
一个长为n的字符串s是回文串的充要条件是，对于 i ∈ [0, n-1]，都有 s[i] == s[n-1-i]



1.暴力法：嵌套循环，时间复杂度O(N^3)

2.动态规划：
大问题是什么？
规模小一点的问题是什么？剩余字串也是回文串
它们之间有什么联系？

怎么去描述子问题呢？显然，一个字串由两端的i、j指针确定，字串s[i:j]是否是回文串，就是子问题。





'''


def countSubstrings(s: str) -> int:
    count = 0
    n = len(s)
    dp = 
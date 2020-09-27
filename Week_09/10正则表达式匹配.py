'''
https://leetcode-cn.com/problems/regular-expression-matching/

10. 正则表达式匹配 （Facebook、微软、字节跳动在半年内面试中考过）

思路：
点号通配符其实很好实现，s 中的任何字符，只要遇到 . 通配符，无脑匹配 就完事了。
星号通配符不好实现，一旦遇到 * 通配符，前面的那个字符可以选择重复一次，可以重复多次，也可以一次都不出现，这该怎么办？
答案很简单，对于所有可能出现的情况，全部穷举一遍，只要有一种情况可以完成匹配，就认为 p 可以匹配 s。
一旦涉及两个字符串的穷举，我们就应该条件反射地想到 动态规划的技巧了。

s 和 p 相互匹配的过程大致是，两个指针 i, j 分别在 s 和 p 上移动，
如果最后两个指针都能移动到字符串的末尾，那么久匹配成功，反之则匹配失败。


dp[i][j] 表示 s 的前 i 个是否能被 p 的前 j 个匹配




星号只会影响它前面的那一个字符，不会影响它后面的字符。所以：
从左往右扫描的话，字符后面是否跟着星号会影响结果，分析起来有点复杂；
从右往左扫描，s、p是否匹配，取决于：最右端是否匹配 + 剩余的字串是否匹配；只是最右端可能是特殊符号，
需要分情况讨论而已。
'''


def isMatch(self, s: str, p: str) -> bool:
    # dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自前 i、j 个字符是否匹配
    # 注意，是前i、j个字符，也就是下标到 s[i-1] 、p[j-1]为止
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True  # s、p都为空串时，肯定匹配

    # s为空串，但p不为空串，要想匹配，只可能是右端是星号，星号干掉一个字符后，把p变成空串
    for j in range(2, len(p) + 1):  # 为什么从2开始？因为当s为空串，p只有一个字符时，肯定不匹配
        # dp[0][j-2]为True ，即 前 j - 3 个字符是匹配的
        # 且p中第j个字符为 *，即p[j-1] 和 p[j-2] 可以消掉
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] in {s[i - 1], '.'}:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                if p[j - 2] in {s[i - 1], '.'}:
                    # or，即其中任何一种匹配，dp[i][j]都算匹配上了
                    # p末尾去掉两个字符，也就是去掉星号及其前面的字符，即不用它们
                    # 或s末尾去掉一个字符,即先用一次
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 2]  # s[i-1] != p[j-1]，则用星号干掉前面的一个字符
    return dp[-1][-1]

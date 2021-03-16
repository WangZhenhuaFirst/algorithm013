'''
https://leetcode-cn.com/problems/longest-common-subsequence/

1143. 最长公共子序列 （亚马逊、字节跳动、谷歌在半年内面试中考过）

思路：
1.为啥这个问题用动态规划解决？
因为子序列类型的问题，穷举出所有可能的结果 都不容易，而动态规划算法做的就是 穷举 + 剪枝。

text1 = {s1,s2,s3,s4...si}
text2 = {t1,t2,t3,t4...tj}
if text1[i] == text2[j]:
    那最大公共子序列就是 {s1,s2,s3...si-1} 和 {t1,t2,t3...tj-1}的最大公共子序列 + 1
else:
    {s1,s2,s3...si-1} 和 {t1,t2...tj} 的最大公共子序列
    {s1,s2,s3...si} 和   {t1,t2...tj-1} 的最大公共子序列
    以上两者中的最大值


'''


def longestCommonSubsequence(text1, text2):
    '''
    递归解法，自顶向下，比较容易理解。
    其实就是暴力解法
    '''
    def dfs(i, j):
        # 递归终止条件
        if i == -1 or j == -1:
            return 0

        if text1[i] == text2[j]:
            # 找到一个lcs中的元素，继续往前找
            return dfs(i-1, j-1) + 1
        else:
            # 谁能让lcs最长，就听谁的
            return max(dfs(i-1, j), dfs(i, j-1))
    return dfs(len(text1)-1, len(text2)-1)


def longestCommonSubsequence(text1, text2):
    '''
    用DP优化时间复杂度
    对于两个字符串的动态规划问题，一般都要像本文一样定义DP table，因为这样容易写出状态转义方程
    '''
    if not text1 or not text2:
        return 0
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]  # 让索引为0的行和列表示空串

    for i in range(1, m+1):
        for j in range(1, n+1):
            # 注意，这里是i-1和j-1
            # 因为循环的范围是[1...m] 和[1...n]
            # 所以i-1 和 j- 1正好对应 [0...m-1]和 [0...n-1]
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 相当于新遍历到的的字符text1[i]、text[j] 没有为lcs做出新贡献
                # 只能用原来最大的lcs
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

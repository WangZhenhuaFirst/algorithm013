'''
https://leetcode-cn.com/problems/edit-distance/

72. 编辑距离 （字节跳动、亚马逊、谷歌在半年内面试中考过）

思路：
1.two-ended BFS
2.DP
「动态规划」告诉我们可以「自底向上」去考虑一个问题，思路是：先想这个问题最开始是什么情况，
这个问题是两个字符串都为空字符的时候，然后逐个地，一个字符一个字符加上去，在加字符的过程中考虑「状态转移」。
由于要考虑空字符，因此状态空间要多设置一行、多设置一列。
base case：从一个字符串变成空字符串，非空字符串的长度就是编辑距离；

思考状态的方法：
1、题目问什么就将什么定义为状态；
2、状态转移方程 怎么好推导，就怎么定义状态；
3、根据经验和问题的特点（只有多做题了）
dp[i][j]代码word1 到 i位置转换成 word2 到 j 位置需要的最少步数


状态转移方程通常是在做分类讨论，而分类讨论的过程，常常利用了这个问题的「最优子结构」。
当word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
当word1[i] != word2[j], dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
dp[i-1][j-1]到dp[i][j]需要进行替换操作，dp[i-1][j]到dp[i][j]需要进行删除操作，
dp[i][j-1] 到d[i][j]需要进行添加操作。
以 word1 为 "horse"，word2 为 "ros"，且 dp[5][3] 为例，
即要将 word1的前 5 个字符转换为 word2的前 3 个字符，也就是将 horse 转换为 ros，因此有：
(1) dp[i-1][j-1]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 2 个字符 ro，
然后将第五个字符 word1[4]（因为下标基数以 0 开始） 由 e 替换为 s（即替换为 word2 的第三个字符，word2[2]）
(2) dp[i][j-1]，即先将 word1 的前 5 个字符 horse 转换为 word2 的前 2 个字符 ro，
然后在末尾补充一个 s，即插入操作
(3) dp[i-1][j]，即先将 word1 的前 4 个字符 hors 转换为 word2 的前 3 个字符 ros，
然后删除 word1 的第 5 个字符 

'''


def minDistance(self, word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)
    dp = [[0] * (n2 + 1) for _ in range(n1+1)]
    for j in range(1, n2 + 1):
        dp[0][j] = j
    for i in range(1, n1 + 1):
        dp[i][0] = i
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return dp[-1][-1]

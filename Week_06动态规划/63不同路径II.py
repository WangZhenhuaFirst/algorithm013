'''
https://leetcode-cn.com/problems/unique-paths-ii/

63. 不同路径II（谷歌、美团、微软在半年内面试中考过）

思路：
自底向上的递归, f(m,n)=f(m−1,n)+f(m,n−1) —— 函数递归调用
自顶向下的递推, dp[i,j]=dp[i−1,j]+dp[i,j−1] —— 填充数组
区别: 
递归时，我不知道每一步中的f(m,n)等于多少，直到推到边界条件，再一层层返回上来；
动态规划时，我是先知道最小、最简单的情况下的数值，在一步步往上。










'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''O(M*N) space'''
        if not obstacleGrid:
            return
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        # 注意，第一行、第一列 也受 前面格子的障碍物的影响，所以必须逐个单独考虑，这和62题不同
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
        # 因为dp用的是 m*n 大小的，所以不能从0 开始遍历，否则 dp[i-1][j] 取不到元素
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''O(N) space'''
        if not obstacleGrid:
            return
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0] * n  # 默认左上角不会有障碍物？？？
        # 如果 dp = [0] * n,但因为dp只有一行，所以不好写
        # 行、列都是从 0 开始遍历的，所以不用特别给第一行、第一列做特殊处理
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j]:  # 障碍物
                    dp[j] = 0
                else:
                    # 当j=0, dp[j-1] 即dp[-1]会取dp的最后一个元素
                    # 给dp多加一列 0，正好就不用判断边界问题了
                    dp[j] = dp[j] + dp[j-1]  # dp[j]代表上边那条路径，dp[j-1]代表左边那条路径
        return dp[-2]  # 注意，这里是 -2 ，不是 -1

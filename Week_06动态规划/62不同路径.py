'''
https://leetcode-cn.com/problems/unique-paths/

62. 不同路径 （Facebook、亚马逊、微软在半年内面试中考过）

思路：
1.排列组合:
要走到右下角一定是向右走m-1步，向下走n-1步。
也就是说总共走m-1+n-1 (m+n-2) 步，其中有m-1步是向右的。
那么这就是一个组合的问题，从m+n-2步中选择m-1步向右，总共有C(m+n-2,m-1)种排列方式。
C(n,m) = n!/(m!*(n-m)!)


2.动态规划：
时间复杂度 O(M*N)
空间复杂度 O(M*N)



'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''排列组合'''
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))

    def uniquePaths(self, m: int, n: int) -> int:
        '''动态规划, O(M*N)'''
        # 第一行和第一列，因为都是边界，只有 1种走法，所以都是1
        # 生成一个第一行、第一列都是 1 的二维数组
        # 和 63题不同的是，本题没有障碍物，所以第一行、第一列肯定是1，可以直接赋值
        dp = [[1] * n] + [[1]+[0] * (n-1) for _ in range(m-1)]  # 注意，是m-1而不是m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        '''
        优化空间复杂度O(2N)
        由于dp[i][j] = dp[i-1][j] + dp[i][j-1]，
        因此只需要保留当前行与上一行的数据
        '''
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return cur[-1]

    def uniquePaths(self, m: int, n: int) -> int:
        '''
        优化空间复杂度O(N)
        cur[j] = cur[j] + cur[j-1] 等价于cur[j] = pre[j] + cur[j-1]
        '''
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]

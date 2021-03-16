'''
https://leetcode-cn.com/problems/minimum-path-sum/

64. 最小路径和（亚马逊、高盛集团、谷歌在半年内面试中考过）

思路：
1.状态定义：设dp为大小m * n 矩阵，其中dp[i][j]的值代表 走到(i,j)的最小路径和。
2.转移方程：走到当前单元格的最小路径和 = “从左方单元格(i-1,j)与上方单元格(i,j-1)走来的两个最小路径和中较小的"
+ 当前单元格值grid[i][j]
其实不需要建立dp矩阵浪费额外空间，直接遍历grid[i][j]修改即可。这是因为
grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
原grid矩阵元素中被覆盖为dp元素后，都处于当前遍历点的左上方，不会再被使用到。

时间复杂度O(M*N):遍历整个grid矩阵元素
空间复杂度O(1)




'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):  # 行
            grid[i][0] += grid[i-1][0]
        for i in range(1, n):  # 列
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

'''
https://leetcode-cn.com/problems/maximal-square/

221. 最大正方形（华为、谷歌、字节跳动在半年内面试中考过）

思路：若某个格子值为1，则以此为右下角的正方形的最大边长为：上面的正方形、左面的正方形或左上的正方形中，
最小的那个，再加上此格。














'''


def maximalSquare(self, matrix: List[List[str]]) -> int:
    'O(M*N)'
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    rows = len(matrix)
    columns = len(matrix[0])
    dp = [[0] * (columns + 1) for _ in range(rows + 1)]
    max_side = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == '1':  # 注意，是字符串，不是数字
                dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
                max_side = max(max_side, dp[i+1][j+1])
    return max_side * max_side

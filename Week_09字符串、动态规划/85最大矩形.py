'''
https://leetcode-cn.com/problems/maximal-rectangle/

85. 最大矩形（谷歌、微软、字节跳动在半年内面试中考过）

思路：













'''


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    '''动态规划 O(N^2*M)'''
    maxarea = 0
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                continue
            # if j else 1，是为了兼容第一列，防止dp[i][j-1]出现dp[i][-1]
            width = dp[i][j] = dp[i][j-1] + 1 if j else 1
            for k in range(i, -1, -1):
                width = min(width, dp[k][j])
                # 计算以(i,j为右下角的最大矩形面积)
                maxarea = max(maxarea, width * (i-k+1))
    return maxarea


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    '''
    动态规划，O(M * N)
    '''
    if not matrix or not matrix[0]:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    left = [-1] * col
    right = [col] * col
    height = [0] * col
    res = 0
    for i in range(row):
        # 每行都重新更新 cur_left 和 cur_right
        cur_left = -1
        cur_right = col

        # 用height记录 第i行为底,第j列高度是多少
        for j in range(col):
            if matrix[i][j] == '1':
                height[j] += 1
            else:
                height[j] = 0

        # 用left记录第i行为底, 第j列左边第一个小于height[j]的位置
        # 实例1，当i=2,j = 2，即matrix[2][2]位置,left[2] = max(left[2], cur_left)
        # 因为这一行都是1， 此时，cur_left = -1, 而括号中的left[2]是上一行时的值，为 1
        # 所以这个位置的left[2]也就是1
        for j in range(col):
            if matrix[i][j] == '1':
                left[j] = max(left[j], cur_left)
            else:
                # 遇到0，赶紧赋值为可能的最小值，
                # 用于下一行遇到1时，与cur_left 比较
                left[j] = -1
                # 遇到0，则cur_left 立即更新为 此列的值
                # 用于下次遇到 1 时，作为左边界
                cur_left = j

        # 用right记录第i行为底, 第j列右边第一个小于height[j]的位置
        for j in range(col - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = col
                cur_right = j

        for j in range(col):  # 是一行行计算的，但每个值都参与了max，所以总会得到最大值
            res = max(res, (right[j] - left[j] - 1) * height[j])
    return res


def maximalRectangle(self, matrix: List[List[str]]) -> int:
    '''与84题一样，栈,遍历每行的高度'''
    if not matrix or not matrix[0]:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    height = [0] * (col + 2)
    res = 0
    for i in range(row):
        stack = []
        # 用height记录 第i行为底,第j列高度是多少
        for j in range(col):
            if matrix[i][j] == '1':
                height[j+1] += 1
            else:
                height[j+1] = 0
        for j in range(col + 2):
            while stack and height[stack[-1]] > height[j]:
                cur = stack.pop()
                res = max(res, (j - stack[-1] - 1) * height[cur])
            stack.append(j)
    return res

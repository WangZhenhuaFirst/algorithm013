'''
https://leetcode-cn.com/problems/valid-sudoku/description/

36. 有效的数独（亚马逊、苹果、微软在半年内面试中考过）

思路：分别建立二维数组 来存储任一个数在相应维度上是否出现过。













'''


def isValidSudoku(board: List[List[str]]) -> bool:
    # 第二维的维数10是为了让下标有9，方便存储数字9
    row = [[0] * 10 for _ in range(9)]
    col = [[0] * 10 for _ in range(9)]
    box = [[0] * 10 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            cur_num = int(board[i][j])
            # j//3 得到 0, 1, 2;还要加上 (i//3) * 3，即0, 3, 6
            if row[i][cur_num] != 0 or col[j][cur_num] != 0 or box[j//3 + (i//3) * 3][cur_num] != 0:
                return False
            row[i][cur_num], col[j][cur_num], box[j //
                                                  3 + (i//3) * 3][cur_num] = 1, 1, 1
    return True

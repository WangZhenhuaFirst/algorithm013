'''
https://leetcode-cn.com/problems/sudoku-solver/#/description

37. 解数独（亚马逊、华为、微软在半年内面试中考过）

思路：和 八皇后问题 类似
1.回溯法
约束编程：在数独上放置一个数字后，立即排除当前 行、列、子方块 对该数字的使用。











'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                # 递归调用，如果到最后 empty 中的元素都能填进去了，说明这种解是可以的
                # 每一层backtrack()都只会调用到这里return True 给上一层了
                if backtrack(iter+1):
                    return True
                # 如果不行，回溯
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False
        backtrack()

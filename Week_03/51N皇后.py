'''
https://leetcode-cn.com/problems/n-queens/

51. N皇后
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

思路：
先把问题分成n个步骤

代码参考：https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms

'''


class Solution:
    def solve_n_queens(self, n):
        result = []

        def dfs(queens, xy_dif, xy_sum):
            p = len(queens)  # p is the index of row
            if p == n:
                result.append(queens)
                return
            for q in range(n):  # q is the index of col
                # queens stores the used cols
                # xy_dif is the diagonal 1
                # xy_sum is the diagonal 2
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]

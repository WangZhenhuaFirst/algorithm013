'''
https://leetcode-cn.com/problems/n-cols/

51. N皇后 （亚马逊、苹果、字节跳动在半年内面试中考过）

思路：先把问题分成n个步骤，回溯算法













'''


class Solution:
    def solve_n_queens(self, n):
        def dfs(cols, xy_dif, xy_sum):
            p = len(cols)  # p is the index of row
            if p == n:  # 递归终止条件
                result.append(cols)  # 每一个cols是一种解决方案
                return

            # 回溯的选择列表
            for q in range(n):  # q is the index of col
                # cols stores the used cols
                # xy_dif is the diagonal 1
                # xy_sum is the diagonal 2
                if q not in cols and p-q not in xy_dif and p+q not in xy_sum:
                    # 每种满足条件的选择都做递归，这才叫回溯
                    dfs(cols+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]

    def solve_n_queens(self, n):
        '''位运算'''

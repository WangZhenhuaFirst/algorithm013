'''
https://leetcode-cn.com/problems/generate-parentheses/

22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

解题思路：
先简化问题，不管是否合法，于是问题变成：2n个格子，每个高个子都可以方左/右括号，共有多少种可能

合法：左括号随时可以加，但最多只能加n个。加右括号的前提是必须先加了相应的左括号，或者说想加右括号时，
必须满足 已经存在的左括号数 > 已经存在的右括号数
'''


class Solution:
    def generate_parenthesis(self, n):
        '''
        :param cur_str: 从根结点到叶子结点的路径字符串
        :param left: 左括号已经使用的个数
        :param right: 右括号已经使用的个数
        '''
        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            if left == n and right == n:
                res.append(cur_str)
                return

            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < left:
                dfs(cur_str + ')', left, right + 1, n)
        dfs(cur_str, 0, 0, n)
        return res

'''
https://leetcode-cn.com/problems/generate-parentheses/

22. 括号生成 (字节跳动在半年内面试中考过)

思路：
先简化、抽象问题，于是问题变成：2n个格子，每个格子都可以放左/右括号，共有多少种可能
每个格子都有左括号或右括号两种可能，所以本题实际上就是个深度/广度优先遍历的问题。
要学会抽象问题，广度优先搜索解决的不是表面上的树、图的问题，而是状态变化问题。

广度优先遍历，需要程序员自己编写节点类，显式使用队列这个数据结构。
深度优先遍历，可以直接使用系统栈，在递归方法执行完成时，系统栈顶就把我们所需要的状态信息直接弹出，
而无需编写节点类和显示使用栈。


符合题目要求：左括号随时可以加，但最多只能加n个。加右括号的前提是必须先加了相应的左括号，或者说想加右括号时，
必须满足 已经存在的左括号数 > 已经存在的右括号数





'''


class Solution:
    def generate_parenthesis(self, n):
        '''
        深度优先遍历
        cur_str: 从根结点到叶子结点的路径字符串
        left: 左括号已经使用的个数
        right: 右括号已经使用的个数
        '''
        def dfs(cur_str, left, right, n):
            # 每一种情况，最终都会返回一次，都append到res中，形成最后的答案
            if left == n and right == n:
                res.append(cur_str)
                return

            # 两个if并列，意思是每个位置都可以填左括号/右括号，也就是都有两种可能
            if left < n:
                dfs(cur_str + '(', left + 1, right, n)

            if right < left:
                dfs(cur_str + ')', left, right + 1, n)

        res = []
        cur_str = ''
        dfs(cur_str, 0, 0, n)
        return res

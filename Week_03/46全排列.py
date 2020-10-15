'''
https://leetcode-cn.com/problems/permutations/
46. 全排列 （字节跳动在半年内面试常考）

思路：

1.暴力解法：n! 种可能



深度优先遍历、递归、栈，它们背后统一的逻辑都是——后进先出








'''


class Solution:
    def permute(self, nums):
        '''
        回溯其实是深度优先遍历特有的一种现象。
        使用编程得到 全排列，就是执行一次深度优先遍历，从树的根节点到叶子节点走通所有的路径
        '''

        def backtrack(nums, path):
            # 递归终结条件
            if not nums:
                res.append(path)
                return

            for i in range(len(nums)):  # 每个元素都可以做开头
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        res = []
        backtrack(nums, [])
        return res

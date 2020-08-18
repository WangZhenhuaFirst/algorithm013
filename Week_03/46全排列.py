'''
https://leetcode-cn.com/problems/permutations/
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/

解题思路：
1.暴力解法：n! 种可能

回溯，指状态重置，可以理解为回到过去、恢复现场。
回溯其实是深度优先遍历特有的一种现象。

使用编程得到全排列，就是执行依次深度优先遍历，从树的根节点到叶子节点走通所有的路径
'''


class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        backtrack(nums, [])
        return res

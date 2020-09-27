'''
https://leetcode-cn.com/problems/permutations/
46. 全排列 （字节跳动在半年内面试常考）

解题思路：
https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-by-powcai-2/

1.暴力解法：n! 种可能


回溯其实是深度优先遍历特有的一种现象。

使用编程得到全排列，就是执行一次深度优先遍历，从树的根节点到叶子节点走通所有的路径







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

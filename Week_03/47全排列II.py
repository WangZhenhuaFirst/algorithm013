'''
https://leetcode-cn.com/problems/permutations-ii/

47. 全排列 II
给定一个可包含重复数字的序列，返回所有不重复的全排列。

思路：
回溯搜索 + 剪枝

在结果中去重？但结果集的元素是多个列表，列表去重不像基本元素去重那么容易。
可以在搜索之前先对数组排序
'''


class Solution:
    def permuteUnique(self, nums):
        if not nums:
            return []

        nums.sort()
        res = []

        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        backtrack(nums, [])
        return res


def permuteUnique_pythonic(self, nums):
    '''
    https://leetcode.com/problems/permutations-ii/discuss/18616/6-lines-Python-Ruby

    To find the last index for inserting new number n into old permutation p, I search for 
    previous instances of n in p. But because index throws an exception if unsuccessful, I add
    a sentinel n at the end

    没看懂是怎么放置重复的？？？
    '''
    perms = [[]]
    for n in nums:
        perms = [p[:i] + [n] + p[i:]
                 for p in perms
                 for i in range((p + [n]).index(n) + 1)]
    return perms

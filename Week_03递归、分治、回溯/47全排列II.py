'''
https://leetcode-cn.com/problems/permutations-ii/

47. 全排列 II （亚马逊、字节跳动、Facebook 在半年内面试中考过）

思路：回溯 + 剪枝
看到 全排列，或者 枚举全部解，等类似的 搜索枚举类型题，基本就是 回溯 没跑了
在结果中去重？但结果集的元素是多个列表，列表去重 不像基本元素去重那么容易。
可以在搜索之前 先对数组排序










'''


class Solution:
    def permuteUnique(self, nums):
        def backtrack(nums, path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                # 这里是在同一层中做剪枝，而不是在递归的不同层做剪枝
                # 既然是在同一层，能取到 nums[i]的时候，当然也就能取到nums[i-1]
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
        nums.sort()
        res = []
        backtrack(nums, [])
        return res


def permuteUnique_pythonic(self, nums):
    '''
    https://leetcode.com/problems/permutations-ii/discuss/18616/6-lines-Python-Ruby

    To find the last index for inserting new number n into old permutation p, I search for 
    previous instances of n in p. But because index throws an exception if unsuccessful, I add
    a sentinel n at the end

    没看懂是怎么防止重复的？？？
    '''
    perms = [[]]
    for n in nums:
        perms = [p[:i] + [n] + p[i:]
                 for p in perms
                 for i in range((p + [n]).index(n) + 1)]
    return perms

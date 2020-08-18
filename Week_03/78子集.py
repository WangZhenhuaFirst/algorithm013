'''
https://leetcode-cn.com/problems/subsets/

78. 子集
给定一组不含重复元素的整数数组nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。

示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


解题思路：
每个数字可以选/不选，2^N 种结果，要确保结果完整且无重复，常用方法：递归、回溯

1.递归
https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).

DFS Visualization:

dfs(nums = [1,2,3], index = 0, path = [], res = [])
|
|__ dfs(nums = [1,2,3], index = 1 , path = [1], res = [[]])
|    |__ dfs(nums = [1,2,3], index = 2 , path = [1,2], res = [[],[1]])
|    	  |__ dfs(nums = [1,2,3], index = 3 , path = [1,2,3], res = [[],[1], [1,2]])
|    	  	   # next: res = [[],[1],[1,2],[1,2,3]]
|    	  	   # for loop will not be executed
|
|__ dfs(nums = [1,2,3], index = 2, path = [[2]], res = [[],[1],[1,2],[1,2,3]])
|    |__ dfs(nums = [1,2,3], index = 3 , path = [[2,3]], res = [[],[1],[1,2],[1,2,3],[2])
|    	  	   # next iteration: res =  [[],[1],[1,2],[1,2,3],[2],[2,3])
|    	  	   # for loop will not be executed
|
|__ dfs(nums = [1,2,3], index = 3, path = [[3]], res =  [[],[1],[1,2],[1,2,3],[2],[2,3])
     	  	   # next iteration: res =  [[],[1],[1,2],[1,2,3],[2],[2,3],[3])
     	  	   # for loop will not be executed

2.迭代：找重复性
https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode/
开始假设输出子集为空，每一步都向子集添加新的元素生成新子集
'''


class Solution:
    def subsets_recursion(self, nums):
        '''
        就遍历下每个位置 要么放要么不放，遍历到j就是计算下次放的位置是j的情况 
        然后从这个位置开始继续算子问题 即i+1之后的数组的子集，
        然后和前面的要拼起来 就是tmp 最后每种tmp都会放到res里

        确实和范型递归的模板不完全很像 没有明确的出口函数吧  
        但这类递归最大的需要理解的地方还是找到子问题，和子问题和父问题的关系 
        然后这个其实也是可以写成模板的形式的

        这题相比于模板比较特别的是 有在for循环里调用递归，确实增加了一些理解的难度 
        但细分类型的话 有一大块题目都会在循环里调用递归 好像好几道排列组合的题都可以那样写

        https://github.com/wfnuser/leetcode/blob/master/78.subset.py 刚刚用模板写了一个 不过应该不如刚刚那个写法快
        '''
        if not nums:
            return []
        n = len(nums)
        res = []

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(0, [])
        return res

    def subsets_iteration(self, nums):
        result = [[]]
        for num in nums:
            result += [r + [num] for r in result]
        return result

'''
https://leetcode-cn.com/problems/subsets/

78. 子集（Facebook、字节跳动、亚马逊在半年内面试中考过）

思路：每个数字可以选/不选，2^N 种结果，要确保结果完整且无重复，常用方法：递归、回溯
DFS和回溯的区别：
DFS是一个劲地往某一个方向搜索，回溯算法是建立在DFS基础之上的。不同的是，达到结束条件后，回溯会
恢复状态，回到上一层，再次搜索。因此回溯和DFS的区别就是 有无状态重置。


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
开始假设输出子集为空，每一步都向子集添加新的元素 生成新子集。
nums = [1,2,3]
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''递归的另一种写法,与77题 组合 基本一样'''
        def backtrack(nums, path):
            res.append(path)  # 每一层一开始，先append，也就是要每一种可能
            for i in range(len(nums)):
                backtrack(nums[i+1:], path + [nums[i]])
        res = []
        backtrack(nums, [])
        return res

    def subsets(self, nums):
        '''
        递归
        https://github.com/wfnuser/leetcode/blob/master/78.subset.py
        '''
        def backtrack(i, tmp):
            res.append(tmp)  # 每一层一开始，先append tmp，也就是要每一种可能
            for j in range(i, len(nums)):  # 每一层都遍历一遍所有可能
                # 因为不要重复的子集，所以递归到下一层时直接 j+1
                backtrack(j + 1, tmp + [nums[j]])
        res = []
        backtrack(0, [])
        return res

    def subsets(self, nums):
        '''迭代'''
        result = [[]]
        for num in nums:
            # 对于nums中的每个元素，都有选/不选两种可能
            # 不选的，result中已经包含了，再加上选的即可
            result += [r + [num] for r in result]
        return result

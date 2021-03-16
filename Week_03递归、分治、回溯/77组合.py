'''
https://leetcode-cn.com/problems/combinations/

77. 组合（微软、亚马逊、谷歌在半年内面试中考过）

思路:如果解决一个问题 有多个步骤，每一个步骤 有多种方法，题目又要我们找出所有的方法，可以使用回溯
组合问题，相对于排列问题而言，不计较一个组合内元素的顺序性（即 [1, 2, 3] 与 [1, 3, 2] 认为是同一个组合），
因此很多时候需要按某种顺序展开搜索，这样才能做到 不重不漏。











'''


def combine(self, n: int, k: int) -> List[List[int]]:
    def backtrack(nums, path):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            # 参数变成了 nums[i+1:]，相当于 选择列表.remove(该选择)，
            # 因为在下一层递归中， for i in range(len(nums[i+1:]))，i 也就不再能取到 该选择了
            # 并且path中取到1个元素后，第二个元素只能取到这之后的了，也就不会用重复的如[1,2]和[2,1]
            # 这就是组合，而不是排列
            backtrack(nums[i+1:], path + [nums[i]])

    res = []
    nums = [i for i in range(1, n+1)]
    backtrack(nums, [])
    return res

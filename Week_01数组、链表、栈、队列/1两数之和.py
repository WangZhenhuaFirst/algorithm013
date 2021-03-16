'''
https://leetcode-cn.com/problems/two-sum/

1. 两数之和（近半年内，字节跳动在面试中考查此题达到 152 次）

思路：
1.暴力方法，两个索引：O(n^2)

2.哈希表：a + b == target 可以转化为：对于数组中每个元素a，数组中是否存在元素 target - b
要想优化时间复杂度，最好的方法就是 以空间换时间，建个哈希表，让每个元素的索引与元素一一对应, O(N)









'''


class Solution:
    def two_sum_bad(self, nums, target):
        '''暴力'''
        for i in range(0, len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twice_hash(self, nums, target):
        dic = {}
        for idx, num in enumerate(nums):
            dic[num] = idx
        for i, num in enumerate(nums):
            j = dic.get(target - num)  # 哈希表查询元素是O(1)的
            if j is not None and i != j:
                return [i, j]

    def one_hash(self, nums, target):
        '''一遍哈希表 O(N)'''
        dic = {}
        for i, num in enumerate(nums):
            # 先判断之前加入哈希表的数值有没有满足需要的
            m = target - num
            if m in dic:
                return [dic[m], i]
            dic[num] = i  # 这句不能放在if之前，解决nums中有重复值或target-num=num的情况

    def one_hash_another(self, nums, target):
        '''
        非常巧妙，
        dic中存的是 target - n，也就是要找的那个数值，
        然后判断nums中是否有这些数值就可以了
        '''
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            dic[target - n] = i

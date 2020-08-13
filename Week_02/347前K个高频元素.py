'''
https://leetcode-cn.com/problems/top-k-frequent-elements/

347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

解题思路：堆处理海量数据的topK很合适，O(NlogK)
1.堆，对于K频率之后的元素不用再去处理。
遍历一遍数组，用哈希表建立数字和频率的映射
维护一个元素数目为K的最小堆
每次将新的元素push进堆，如果堆的长度大于K，将最小值出堆
'''

import heapq


class Solution:
    def topk_frequent(self, nums, k):
        if len(nums) == 1:
            return nums

        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        h = []
        for key in d:
            heapq.heappush(h, (d[key], key))
            if len(h) > k:
                heapq.heappop(h)

        res = []
        while h:
            res.append(heapq.heappop(h)[1])
        return res

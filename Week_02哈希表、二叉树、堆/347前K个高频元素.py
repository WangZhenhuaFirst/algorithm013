'''
https://leetcode-cn.com/problems/top-k-frequent-elements/

347. 前 K 个高频元素（亚马逊在半年内面试中常考）

思路：堆 处理 海量数据的topK 很合适，O(NlogK)
1.堆，对于K频率之后的元素 不用再去处理。
遍历一遍数组，用哈希表建立数字和频率的映射
维护一个元素数目为K的最小堆
每次将新的元素push进堆，如果堆的长度大于K，将最小值出堆









'''

import heapq


class Solution:
    def topk_frequent(self, nums, k):
        '''O(NlogK)'''
        if len(nums) == 1:
            return nums

        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        h = []
        for key in dic:
            heapq.heappush(h, (dic[key], key))
            if len(h) > k:
                heapq.heappop(h)

        return [x[1] for x in h]

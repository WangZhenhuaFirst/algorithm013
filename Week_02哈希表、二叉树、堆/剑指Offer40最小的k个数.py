'''
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

剑指 Offer 40. 最小的k个数（字节跳动在半年内面试中考过）

思路：
1.sort: 时间复杂度为O(NlogN),即排序的时间复杂度；空间复杂度为O(logN),因为排序需要额外的空间复杂度
2.heap: O(NlogK)
3.快排










'''

import heapq


class Solution:
    def get_least_numbers_sort(self, arr, k):
        arr.sort()
        return arr[0:k]

    def get_least_numbers_heap(self, arr, k):
        '''
        Python语言中的堆为小根堆
        首先将前K个数插入小根堆，然后从K+1个元素开始 跟小根堆的第一个元素比较 O(NlogK)
        '''
        if k == 0:
            return []

        # 为什么取负值呢？负值越小，说明原值越大，也就是 这K个数中 原值最大的位于 堆顶
        # 新进来的值如果比它小，就替代它，替代到最后，堆中就是最小的K个值了
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        '''
        将全部数据放入小根堆，然后循环逐一取出前K个元素，O（KlogN)，取每个元素的时间复杂度是logN;
        '''
        if k == 0:
            return []
        q = []
        for num in arr:
            heapq.heappush(q, num)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(q))
        return res

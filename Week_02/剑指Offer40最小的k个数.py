'''
剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

解题思路：
1.sort: 时间复杂度为O(NlogN),即排序的时间复杂度；空间复杂度为O(logN),因为排序所需额外的空间复杂度
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
        将全部数据放入小根堆，然后循环逐一取出前K个元素，O（KlogN)，取每个元素的时间复杂度是logN;
        或者首先将前K个数插入小根堆，然后从K+1个元素开始跟小根堆的第一个元素比较 O（NlogK)
        '''
        if k == 0:
            return []

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans

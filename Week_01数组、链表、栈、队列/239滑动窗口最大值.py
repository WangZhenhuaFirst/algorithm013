'''
https://leetcode-cn.com/problems/sliding-window-maximum/

239. 滑动窗口最大值（亚马逊在半年内面试常考）

思路：
1.暴力,嵌套两个循环:O(N * K)

2.deque：O(N) 滑动窗口类型的问题，都可以用队列解决
双向队列可以从两端 以常数时间复杂度 压入/弹出元素
如何想到用双端队列的？前面的数离开，后面的数 加进来

3. 堆，PriorityQueue:O(NlogN)






'''

import heapq


class Solution:
    def max_sliding_window_bad(self, nums, k):
        '''暴力'''
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]

    def max_sliding_window_good(self, nums, k):
        '''双向队列'''
        if k == 1:
            return nums

        res = []
        n = len(nums)
        window = []
        for i in range(n):
            # 每次都先把多余的数弹出去
            # 窗口/双端队列中最多只能容纳k个数，所以当i>=k时，要先去掉 不属于当前窗口的数
            if i >= k and i - k == window[0]:
                window.pop(0)
            # 每个数新进来时都比较一下大小，把肯定不是最大值的弹出，就不用max了
            # 如果滑动窗口非空，新进来的数比队列里已经存在的数还大
            # 说明已经存在的数一定不会是滑动窗口的最大值，则将它们弹出
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)  # 每个i都是要append到window中的,因为新的数总是最靠右的
            if i >= k - 1:  # 每遍历到一个新的i，或者说每滑动一步，总要有一个最大值产生
                res.append(nums[window[0]])
        return res

        def max_sliding_window_heap(self, nums, k):
            if k == 1:
                return nums
            res, heap = [], []
            for i in range(len(nums)):
                # 因为Python是小顶堆，所以加个负号
                heapq.heappush(heap, (-nums[i], i))
                if i >= k - 1:  # 从这里开始，才填满了窗口，才开始有最值
                    # heapq.heappop(heap) 移除的是最小值，只有在 heap[0][1] < i + 1 - k时，
                    # 才需要移除它，因为只有这时候它才不属于本窗口，才不应该参与本窗口最值的竞选
                    # 至于之前的窗口的非最值，是否移除无所谓，反正又不参与最值的竞选
                    # 判断一下while heap,是为了防止 heap[0][1] 取不到值
                    while heap and heap[0][1] < i - k + 1:
                        heapq.heappop(heap)
                    res.append(-heap[0][0])
            return res

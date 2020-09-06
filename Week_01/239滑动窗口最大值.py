'''
239. 滑动窗口最大值
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

进阶：
你能在线性时间复杂度内解决此题吗？


解题思路：
1.暴力,嵌套两个循环:O(N * K)

2.deque：O(N) 滑动窗口类型的问题，都可以用队列解决
双向队列可以从两端以常数时间复杂度压入/弹出元素

如何想到用双端队列的？
前面的数离开，后面的数加进来


3. 堆，PriorityQueue:O(NlogN)




'''

from collections import deque
import heapq


class Solution:
    def max_sliding_window_bad(self, nums, k):
        '''暴力'''
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]

    def max_sliding_window_good(self, nums, k):
        '''双向队列'''
        # 特例
        if k == 1:
            return nums
        res = []
        n = len(nums)
        window = deque()
        for i in range(n):
            # 窗口/双端队列中最多只能容纳k个数，所以当i>=k时，要先去掉多余的数，或者说不属于当前窗口的数
            if i >= k and i - k == window[0]:
                window.popleft()
            # 如果滑动窗口非空，新进来的数比队列里已经存在的数还大
            # 说明已经存在的数一定不会是滑动窗口的最大值，则将它们弹出
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

        def max_sliding_window_heap(self, nums, k):
            if k == 1:
                return nums
            res, heap = [], []
            for i in range(len(nums)):
                # 因为Python是小顶堆，所以加个负号
                heapq.heappush(heap, (-nums[i], i))
                if i + 1 >= k:
                    # heapq.heappop(heap) 移除的是最小值，只有在 heap[0][1] < i + 1 - k时，
                    # 才需要移除它，因为只有这时候它才不属于本窗口，才不应该参与本窗口最值的竞选
                    # 至于之前的窗口的非最值，是否移除无所谓，反正又不参与最值的竞选
                    while heap and heap[0][1] < i + 1 - k:
                        heapq.heappop(heap)
                    res.append(-heap[0][0])
            return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = s.max_sliding_window_good(nums, k)
    print(result)

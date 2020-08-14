'''
https://leetcode-cn.com/problems/ugly-number-ii/

解题思路：
丑数即一个数等于 2^x * 3^y * 5^z, x、y、z 可以为 0
任何丑数乘以2、3、5,结果也是丑数。

1.堆/优先队列：O(NlogN)  求第n小的丑数，当然就可以用最小堆
https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode/
从堆中包含一个数字开始：1，去计算下一个丑数。
将1从堆中弹出然后将三个数字添加到堆中：1×2, 1×3，1×5。现在堆中最小的数字是 2。
为了计算下一个丑数，要将2从堆中弹出然后添加三个数字：2×2, 2×3，2×5。
重复该步骤计算所有丑数。在每个步骤中，弹出堆中最小的丑数 k，并在堆中添加三个丑数：k×2, k×3，k×5。





2.动态规划：O(N)
'''

import heapq


class Solution:
    def nth_ugly_number(self, n):
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]
        for _ in range(n):
            cur_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = cur_ugly * f
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return cur_ugly

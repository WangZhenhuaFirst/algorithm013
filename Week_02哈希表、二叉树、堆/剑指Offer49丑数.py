'''
https://leetcode-cn.com/problems/ugly-number-ii/

剑指 Offer 49. 丑数（字节跳动在半年内面试中考过）

思路：
丑数即一个数等于 2^x * 3^y * 5^z, x、y、z 可以为 0
任何丑数乘以2、3、5,结果也是丑数。

1.堆/优先队列：O(NlogN)  求第n小的丑数，当然就可以用 最小堆
https://leetcode-cn.com/problems/ugly-number-ii/solution/chou-shu-ii-by-leetcode/
从堆中包含一个数字开始：1，去计算下一个丑数。
将1从堆中弹出然后将三个数字添加到堆中：1×2, 1×3，1×5。现在堆中最小的数字是 2。
为了计算下一个丑数，要将2从堆中弹出然后添加三个数字：2×2, 2×3，2×5。
重复该步骤计算所有丑数。在每个步骤中，弹出 堆中最小的丑数 k，并在堆中添加三个丑数：k×2, k×3，k×5。



2.动态规划：O(N)
'''

import heapq


class Solution:
    def nth_ugly_number(self, n):
        '''堆'''
        heap = []
        heapq.heappush(heap, 1)

        seen = set()
        seen.add(1)

        factors = [2, 3, 5]
        for _ in range(n):
            cur_ugly = heapq.heappop(heap)
            for f in factors:
                new_ugly = cur_ugly * f
                if new_ugly not in seen:  # 需要去重，比如 2 * 3 == 3 * 2，会有重复
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return cur_ugly

    def nthUglyNumber(self, n: int) -> int:
        '''
        动态规划, dp[i]表示第i个丑数
        '''
        dp = [0] * n
        dp[0] = 1
        f2 = 0
        f3 = 0
        f5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[f2], 3 * dp[f3], 5 * dp[f5])
            if dp[i] == 2 * dp[f2]:  # 已经入选的组合，就不需要再参与了
                f2 += 1
            if dp[i] == 3 * dp[f3]:
                f3 += 1
            if dp[i] == 5 * dp[f5]:
                f5 += 1
        return dp[-1]

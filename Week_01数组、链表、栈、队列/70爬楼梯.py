'''
https://leetcode-cn.com/problems/climbing-stairs/

70. 爬楼梯 （阿里巴巴、腾讯、字节跳动在半年内面试常考）

思路：
看完题目后，如果完全懵逼，怎么办？
1.想一下 暴力求解 的方法 可行吗？
2.想 最简单的情况 是怎样的：
一级台阶：1
二级台阶：2
三级台阶：3
四级台阶：从前往后想，很难想明白了，怎么办？

计算机是人类发明的，它没那么复杂，它只会：
1.顺序执行
3.if else
3.for/while 或 recursion
其实世界上绝大部分事情 也就这三种情况

所以，如果算法能解决这个问题，那这个问题肯定能用以上三种方法解决。
顺序执行和if else 不用说了，你一眼就能看出来。
如果是没法一下子想清楚的问题，就要找它的 最近重复子问题，一直分解下去，
最终就是个简单到 一下就能想明白的问题了

四级台阶的问题，最后一步 只有两种可能，从第三级一步跨上来/从第二级一步跨上来。
这样想既不会漏掉情况，也不会有重复的情况。
所以 f(4) = f(2) + f(3)
所以，这是个 递归问题

这个问题从前往后想 是想不明白的，因为你需要把所有情况都列举出来，
而随着楼梯阶数的增加，人脑就晕了。
但从后往前想，虽然我把f(n) 分解为 f(n-1) 和 f(n-2)的时候，
还不知道f(n-1) 和 f(n-2)具体的值，但我可以 假设我知道，
然后继续分解下去，直到f(2)和f(1)这样的 简单问题

可以说是 从后往前想，也可以说是 总——分，先不管细节，先想总体。
或者说是 自顶向下的思考方式

https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
'''


class Solution:
    def climb_stairs(self, n):
        '''动态规划'''
        if n <= 2:
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n + 1):
            f3 = f1 + f2
            # 以下两行的顺序不能互换
            f1 = f2
            f2 = f3
        return f3

    def climb_stairs(self, n):
        '''另一种写法'''
        if n <= 2:
            return n
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f[n-1]

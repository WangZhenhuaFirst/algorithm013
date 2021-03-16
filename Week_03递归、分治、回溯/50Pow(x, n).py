'''
https://leetcode-cn.com/problems/powx-n/

50. Pow(x, n) （Facebook 在半年内面试常考）

思路：
1.暴力：O(N) x 乘 n 次，即循环


2.分治:O(logN)  二分的时间复杂度为 对数级别
x^n = x^n/2 * x^n/2
或
x^n = (x^2)^n/2 = (x*x)^n/2

递归template:
1.terminator
2.process:split your big problem
3.drill down:subproblems, merge subresult
4.reverse states
'''


class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''暴力'''
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x
        ans = 1
        for i in range(n):
            ans *= x
        return ans

    def myPow(self, x: float, n: int) -> float:
        '''分治'''
        # 终结条件/边界条件是 n = 0 和 n = 1
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x

        # 分
        half = self.myPow(x, n // 2)

        # 合 merge,分治的每一层都需要合
        if n % 2 == 1:
            return half * half * x
        return half * half

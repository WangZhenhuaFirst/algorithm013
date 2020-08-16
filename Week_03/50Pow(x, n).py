'''
https://leetcode-cn.com/problems/powx-n/

50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数。


1.暴力：O(N)
x 乘 n 次，即循环


2.分治:O(logN)  二分的时间复杂度为对数级别
x^n = x^n/2 * x^n/2
https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/

递归template:
1.terminator
2.process:split your big problem
3.drill down:subproblems, merge subresult
4.reverse states
'''


class Solution:
    def my_pow_recursion(self, x: float, n: int) -> float:
        # 边界条件是 n = 0 和 n = 1
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n < 0:
            return 1 / self.my_pow_recursion(x, -n)
        if n % 2 == 0:
            return self.my_pow_recursion(x*x, n/2)
        else:
            return x * self.my_pow_recursion(x, n - 1)

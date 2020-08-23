'''
https://leetcode-cn.com/problems/sqrtx/

69. x 的平方根

思路：
1.二分查找： y = x^2 , x > 0的部分 是单调递增的，且有上下界(0,y)


2.牛顿迭代法：
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        '''二分查找'''
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def mySqrt(self, x: int) -> int:
        '''这种写法比较容易确定mid，不像上面那个方法不好确定最终结果是left 还是 right'''
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1

    def mySqrt(self, x):
        '''牛顿迭代法'''
        if x == 0 or x == 1:
            return x
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)

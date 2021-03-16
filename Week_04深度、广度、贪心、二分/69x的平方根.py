'''
https://leetcode-cn.com/problems/sqrtx/

69. x 的平方根（字节跳动、微软、亚马逊在半年内面试中考过）

思路：
1.二分查找： y = x^2 , x > 0的部分 是单调递增的，且有上下界(0,y)


2.牛顿迭代法：









'''


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        二分查找,就很标准的写法
        '''
        if x == 0 or x == 1:
            return x
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            tmp = mid * mid
            if tmp == x:
                return mid
            elif tmp > x:
                right = mid - 1
            else:
                left = mid + 1
        # 如果存在 mid * mid == x,那就直接return mid 了
        # 因为while 循环的条件是 left <= right, 所以停止循环的情况会是 left > right
        # 也就是说 上次循环的情况是 mid * mid < x, 所以执行了 left = mid + 1 > right
        return right

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

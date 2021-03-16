'''
https://leetcode-cn.com/problems/valid-perfect-square/

367. 有效的完全平方数（亚马逊在半年内面试中考过）

思路：













'''


def isPerfectSquare(self, num: int) -> bool:
    '''
    暴力解法，O(sqrt(N))
    i从1开始
    '''
    i = 1
    while i * i < num:
        i += 1
    return i * i == num


def isPerfectSquare(self, num: int) -> bool:
    '''
    等差数列 O(sqrt(N))
    1 + 3 + 5 + 7 + (2N - 1) = N^2
    '''
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


def isPerfectSquare(self, num: int) -> bool:
    '''
    二分查找 O(log(N))
    '''
    left = 1
    right = num
    while left <= right:
        mid = left + (right - left) // 2
        tmp = mid * mid
        if tmp == num:
            return True
        elif tmp < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

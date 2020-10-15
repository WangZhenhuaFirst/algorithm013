'''
https://leetcode-cn.com/problems/reverse-bits/

190. 颠倒二进制位 （苹果在半年内面试中考过）

思路：













'''


def reverseBits(self, n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) + (n & 1)  # n & 1 能取到最后一位数字
        n >>= 1
    return res

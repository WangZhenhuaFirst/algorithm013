'''
https://leetcode-cn.com/problems/power-of-two/

231. 2的幂 （谷歌、亚马逊、苹果在半年内面试中考过）

思路：
1 = 1
2 = 10
4 = 100
8 = 1000
'''


def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

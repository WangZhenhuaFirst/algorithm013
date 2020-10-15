'''
https://leetcode-cn.com/problems/power-of-two/

231. 2的幂 （谷歌、亚马逊、苹果在半年内面试中考过）

思路：
1 = 1
2 = 10
4 = 100
8 = 1000
规律：2的幂次方的 二进制表示 中有且仅有一个1








'''


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1  # 如果是，证明n能一直被2整除


def isPowerOfTwo(n: int) -> bool:
    # n 和 n-1 唯一的不同就是最低位的1，所以这会清零 最低位的 1
    # 这里也就是会清掉唯一一个1
    return n > 0 and (n & (n - 1)) == 0

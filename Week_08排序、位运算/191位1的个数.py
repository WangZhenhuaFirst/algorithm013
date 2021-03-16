'''
https://leetcode-cn.com/problems/number-of-1-bits/

191. 位1的个数（Facebook、苹果在半年内面试中考过）

思路：













'''


def hammingWeight(self, n: int) -> int:
    '''手动循环'''
    n = bin(n)  # 返回的n是个字符串
    count = 0
    for c in n:
        if c == '1':
            count += 1
    return count


def hammingWeight(self, n: int) -> int:
    '''
    进行十进制转二进制的过程，
    每次对2取余 判断是否为1，是的话count加1
    '''
    count = 0
    while n:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count


def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        # n与1 进行与运算，将得到n的最低位数字。
        # 因为1的二进制 就是 0001
        # 他与任何二进制数进行与运算，得到的就是这个数的最低位，最低位可能是0，也可能是1
        count += n & 1
        n >>= 1  # 将n右移一位,也就是扔掉n的最低位数字
    return count


def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += 1
        # n 和 n-1 唯一的不同就是最低位的1，
        # 所以这会清零 最低位的 1，所以本方法只需循环 1的个数次
        n = n & (n-1)
    return count

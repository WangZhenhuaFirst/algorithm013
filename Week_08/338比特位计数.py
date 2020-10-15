'''
https://leetcode-cn.com/problems/counting-bits/description/

338. 比特位计数（字节跳动、Facebook、MathWorks 在半年内面试中考过）

思路：
奇数：二进制表示中，奇数一定比前面那个偶数多一个1，因为多的就是最低位的1
    0 = 0   1 = 1
    2 = 10  3 = 11
偶数：二进制表示中，偶数中 1 的个数一定和除以2 之后的那个数一样多，因为最低位是0，除以2就是右移一位，
也就是把最低位的0抹掉。
    2 = 10   4 = 100  8 = 1000
    3 = 11   6 = 110  12 = 1100
'''


def countBits(self, num: int) -> List[int]:
    res = [0, 1, 1]
    for n in range(3, num+1):
        if n & 1 == 1:  # 奇数
            res.append(res[-1] + 1)
        else:
            res.append(res[n//2])
    # 之所以不直接输出 res，是因为 num可能小于2，而我们一开始初始化res 为[0, 1, 1]
    return res[0:num+1]


def countBits(self, num: int) -> List[int]:
    '''
    动态规划
    十进制数转化为二进制的方法：除二取余，倒序排列
    dp[n] = dp[n//2] + n%2
    '''
    dp = [0]
    for n in range(1, num+1):  # 0不用处理
        # n >> 1 相当于 n//2, 而dp[n//2]中存的是 上一个数的二进制形式中 1的个数
        # n & 1，是在取余数，如果是奇数，加 余数1；如果是偶数，加 余数0
        dp.append(dp[n >> 1] + (n & 1))
    return dp

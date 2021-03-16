'''
https://leetcode-cn.com/problems/plus-one/

66. 加一（谷歌、字节跳动、Facebook 在半年内面试中考过）

思路:













'''


def plusOne(self, digits: List[int]) -> List[int]:
    sums = 0
    n = len(digits)
    for i in range(n):
        sums += 10**(n-i-1) * digits[i]
    sums_str = str(sums + 1)
    return [int(j) for j in sums_str]


def plusOne(self, digits: List[int]) -> List[int]:
    # 从最低位开始做加法运算
    n = len(digits)
    for i in range(n-1, -1, -1):
        # 只要最后一位不是9，就只需要给最后一位加一，然后直接返回
        # 如果最后一位是9，那就把最后一位赋值为0，然后看前一位是否是9
        if digits[i] != 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    ans = [0] * (n + 1)
    ans[0] = 1
    return ans

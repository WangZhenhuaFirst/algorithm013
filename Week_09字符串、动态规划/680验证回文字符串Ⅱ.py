'''
https://leetcode-cn.com/problems/valid-palindrome-ii/

680. 验证回文字符串Ⅱ （Facebook 在半年内面试中常考）

思路：













'''


def validPalindrome(self, s: str) -> bool:
    if s == s[::-1]:
        return True

    def is_valid(s):
        return s == s[::-1]

    left = 0
    right = len(s) - 1
    while left < right:
        # 如果遇到的元素不相等，也就是遇到了 构成回文串的障碍，应进行处理
        if s[left] != s[right]:
            # 一个是去掉了left，一个是去掉了 right，并且其之间的肯定是回文了
            return is_valid(s[left+1:right+1]) or is_valid(s[left:right])
        else:
            left += 1
            right -= 1
    return True

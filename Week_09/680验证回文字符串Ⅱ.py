'''
https://leetcode-cn.com/problems/valid-palindrome-ii/

680. 验证回文字符串 Ⅱ （Facebook 在半年内面试中常考）

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
        if s[left] != s[right]:
            return is_valid(s[left+1:right+1]) or is_valid(s[left:right])
        left += 1
        right -= 1
    return True

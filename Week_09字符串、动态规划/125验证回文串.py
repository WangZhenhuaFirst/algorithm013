'''
https://leetcode-cn.com/problems/valid-palindrome/

125. 验证回文串（Facebook 在半年内面试中常考）

思路：













'''


def isPalindrome(self, s: str) -> bool:
    '''
    使用语言中的 字符串翻转API 得到逆序字符串
    '''
    sgood = ''.join(c.lower() for c in s if c.isalnum())
    return sgood == sgood[::-1]


def isPalindrome(self, s: str) -> bool:
    sgood = ''.join(c.lower() for c in s if c.isalnum())
    n = len(sgood)
    left = 0
    right = n - 1
    while left < right:
        if sgood[left] != sgood[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindrome(self, s: str) -> bool:
    '''在原字符串上直接判断'''
    n = len(s)
    left = 0
    right = n - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right:  # 这里只能用if，不能用while 因为每次都要先走到字母、数字的位置，才能比较是否相同
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True

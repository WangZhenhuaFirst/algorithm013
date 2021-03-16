'''
https://leetcode-cn.com/problems/reverse-only-letters/

917. 仅仅反转字母 （字节跳动在半年内面试中考过）

思路：













'''


def reverseOnlyLetters(self, S: str) -> str:
    '''双指针'''
    left = 0
    right = len(S) - 1
    s = list(S)
    while left < right:
        while left < right and not s[left].isalpha():
            left += 1
        while left < right and not s[right].isalpha():
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)


def reverseOnlyLetters(self, S: str) -> str:
    letters = [c for c in S if c.isalpha()]
    ans = []
    for c in S:
        if c.isalpha():
            ans.append(letters.pop())
        else:
            ans.append(c)
    return ''.join(ans)

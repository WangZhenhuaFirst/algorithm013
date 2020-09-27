'''
https://leetcode-cn.com/problems/reverse-only-letters/

917. 仅仅反转字母 （字节跳动在半年内面试中考过）

思路：













'''


def reverseOnlyLetters(self, S: str) -> str:
    '''双指针'''
    l = 0
    r = len(S) - 1
    s = list(S)
    while l < r:
        while l < r and not s[l].isalpha():
            l += 1
        while l < r and not s[r].isalpha():
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
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

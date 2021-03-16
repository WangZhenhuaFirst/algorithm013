'''
https://leetcode-cn.com/problems/reverse-string/

344. 反转字符串 （亚马逊、谷歌、苹果在半年内面试中考过）

思路：













'''


def reverseString(self, s: List[str]) -> None:
    '''双指针法'''
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

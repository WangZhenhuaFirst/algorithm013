'''
https://leetcode-cn.com/problems/first-unique-character-in-a-string/

387. 字符串中的第一个唯一字符 （亚马逊、微软、Facebook 在半年内面试中考过）

思路：
1.暴力嵌套循环O(N^2)
2.哈希表 O(N)











'''


def firstUniqChar(self, s: str) -> int:
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1


def firstUniqChar(self, s: str) -> int:
    for c in s:
        if s.find(c) == s.rfind(c):
            return s.find(c)
    return -1

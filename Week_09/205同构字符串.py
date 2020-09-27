'''
https://leetcode-cn.com/problems/isomorphic-strings/

205. 同构字符串 （谷歌、亚马逊、微软在半年内面试中考过）

思路：













'''


def isIsomorphic(self, s: str, t: str) -> bool:
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        else:
            if t[i] in dic.values():  # 这是关键，看有没有一对多的现象
                return False
            else:
                dic[s[i]] = t[i]
    return True


def isIsomorphic(self, s: str, t: str) -> bool:
    '''
    index返回的总是 第一个匹配项的索引，
    如果s中有重复字符，那t的相应位置，也必须是相应的重复字符，索引才会相等
    '''
    for i in range(len(s)):
        if s.index(s[i]) != t.index(t[i]):
            return False
    return True

'''
https://leetcode-cn.com/problems/longest-common-prefix/description/

14. 最长公共前缀 （亚马逊、谷歌、Facebook 在半年内面试中考过）

思路：
1.将所有字符串对齐，一个个字符分别比较
2.Trie 树











'''


def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ''
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
    return strs[0]


def longestCommonPrefix(self, strs: List[str]) -> str:
    '''取一个单词，和后面单词比较，看与每个单词相同的最长前缀是多少'''
    if not strs:
        return ""
    res = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(res) != 0:  # 如果不包含，则find会返回-1
            res = res[0:len(res)-1]  # 会每次从后面删掉一个元素
    return res


def longestCommonPrefix(self, strs: List[str]) -> str:
    '''按字典排序数组，比较第一个和最后一个单词，有多少前缀相同'''
    if not strs:
        return ''
    strs.sort()  # sort()是按字母顺序排序的
    n = len(strs)
    a = strs[0]
    b = strs[n-1]
    res = ""
    for i in range(len(a)):
        if i < len(b) and a[i] == b[i]:
            res += a[i]
        else:
            break
    return res


def longestCommonPrefix(self, strs: List[str]) -> str:
    '''Python 特性，取每一个单词的同一位置的字母，看是否相同'''
    res = ''
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res

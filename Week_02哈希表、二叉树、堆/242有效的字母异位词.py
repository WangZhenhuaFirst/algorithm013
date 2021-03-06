'''
https://leetcode-cn.com/problems/valid-anagram/

242. 有效的字母异位词 （Facebook、亚马逊、谷歌在半年内面试中考过）

思路：
1.暴力，sort，比较sorted_str 是否相等？ O(NlogN)
2.哈希表，用 map 统计每个字符的频次











'''


class Solution:
    def is_anagram_bad(self, s, t):
        '''直接调用编程语言的sort方法'''
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def is_anagram_good(self, s, t):
        '''哈希表,计数排序'''
        if len(s) != len(t):
            return False
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

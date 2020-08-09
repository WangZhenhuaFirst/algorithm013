'''
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1
输入: s = "anagram", t = "nagaram"
输出: true


解题思路：
1.暴力，sort，比较sorted_str 是否相等？ O(NlogN)
2.哈希表，用 map 统计每个字符的频次
'''


class Solution:
    def is_anagram_bad(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def is_anagram_good(self, s, t):
        if len(s) != len(t):
            return False
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2


if __name__ == "__main__":
    so = Solution()
    s = "anagram"
    t = "nagaram"
    # res = so.is_anagram_bad(s, t)
    res = so.is_anagram_good(s, t)
    print(res)

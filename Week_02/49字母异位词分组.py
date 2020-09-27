'''
https://leetcode-cn.com/problems/group-anagrams/

49. 字母异位词分组 （亚马逊在半年内面试中常考）
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。

解题思路：
1.建立哈希表，以排序后的字串作为key，同类的原字串作为value
时间复杂度为O(N * KlogK)，N 是 输入数组strs的长度，K是strs中字符串的最大长度，
外部循环的时间复杂度为O(N)，对每个字符串排序的时间复杂度为O(KlogK)

2.对每个字符的出现次数进行计数


两种方法很相似，都是将一个 哈希表。不同之处是，一个是对字符串进行排序做为key，一个是计算各个字母出现的
次数作为key
'''


class Solution:
    def group_anagrams(self, strs):
        if not strs:
            return []
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return list(dic.values())

    def group_anagrams_count(self, strs):
        dic = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)] = dic.get(tuple(count), []) + [s]
        return list(dic.values())


if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = s.group_anagrams_count(strs)
    print(res)

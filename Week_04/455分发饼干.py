'''
https://leetcode-cn.com/problems/assign-cookies/description/

455. 分发饼干

思路：优先满足胃口小的小朋友的需求












'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        # 升序排序
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        while i < len(g) and j < len(s):
            # 此饼干可以满足此小朋友的胃口
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

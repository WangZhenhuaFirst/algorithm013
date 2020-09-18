'''
https://leetcode-cn.com/problems/merge-intervals/

56. 合并区间（Facebook、字节跳动、亚马逊在半年内面试中常考）

思路：区间类的问题，最好画图来辅助思考。
先将区间按左端点排好序，
然后合并重叠的区间：如何判断两个区间是否重叠？比如 a = [1, 4], b= [2, 3]
当 a[1] >= b[0],说明两个区间有重叠

'''


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort()
    res = [intervals[0]]
    for s in intervals[1:]:
        if res[-1][1] < s[0]:
            res.append(s)
        else:
            res[-1][1] = max(s[1], res[-1][1])
    return res

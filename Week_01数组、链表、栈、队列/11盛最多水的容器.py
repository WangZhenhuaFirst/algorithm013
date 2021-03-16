'''
https://leetcode-cn.com/problems/container-with-most-water/

11. 盛最多水的容器（腾讯、百度、字节跳动在近半年内面试常考）

思路：
面积 = 长 * 高
长 = 两个数的差的绝对值
高 = 两个数中较小的那个

注意：题目中说“在坐标内画n条垂直线”，既然是线，就是没有宽度的，或者说宽度为0，也就是不会占用水的空间

1.枚举,嵌套循环 O(n^2)

2.左右边界，向中间收——左右夹逼：O(n)
关键字：左右两边
模式识别：需要移动左右两头的问题 可以考虑 双指针i,j

如何移动指针？要看面积的特点：
- 相同高度下，两边的距离越远越好
- 面积受限于较短边

先取长度最大的，也就是最左、最右的两个边，
然后比较左右两个边的高度，短的那个则向内更新。
高的不用更新，因为越向内，长度是越小的，如果更新高的，
即使新的边更高，而因为面积受限于较短边，也就是 还是会受限于原来的短边，则面积肯定只会更小。
所以，只有更新短的 才有可能 面积更大
'''


class Solution:
    def max_area_bad(self, height):
        max_area = 0
        n = len(height)
        for i in range(n - 1):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area

    def max_area_good(self, height):
        max_area = 0
        # 这才叫双指针，两个for循环那叫嵌套循环
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

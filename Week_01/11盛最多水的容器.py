'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49


解题思路：
面积 = 长 * 高
长 = 两个数的差的绝对值
高 = 两个数中较小的那个

1.枚举,嵌套循环 O(n^2)

2.左右边界，向中间收——左右夹逼：O(n)
关键字：左右两边
模式识别：需要移动左右两头的问题 可以考虑双指针i,j

如何移动指针？要看面积的特点：
- 相同高度下，两边的距离越远越好
- 面积受限于较短边

先取长最大的，也就是最左、最右的两个边，
然后比较左右两个边的高度，短的那个则向内更新。
高的不用更新，因为越向内，长度是越小的，如果更新高的，
即使新的边更高，而因为面积受限于较短边，也就是还是会受限于原来的短边，则面积肯定只会更小。
所以，只有更新短的才有可能面积更大
'''


class Solution:
    def max_area_bad(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area

    def max_area_good(self, height):
        max_area = 0
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


if __name__ == "__main__":
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.max_area_bad(height))
    print(s.max_area_good(height))

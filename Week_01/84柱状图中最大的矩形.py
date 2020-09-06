'''
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例:
输入: [2,1,5,6,2,3]
输出: 10


解题思路：
1.暴力方法1， O(N^3)
for i -> 0, n-2
    for j -> i+1, n-1
    (i, j) -> 以i、j为左右边界，然后找这之间的最小高度，也需要遍历 -> area
    update max_area

2.暴力方法2，有所改善：时间复杂度O(N^2)，空间复杂度O(1)
for i -> 0, n-1
    找其 left bound, right bound(第一个比i短的)
    area = height[i] * (right - left)
    update max_area
依次遍历柱形的高度，对于每个高度分别向两边扩散，求出以当前高度为矩形的最大宽度是多少

3.stack：以空间换时间
要搞清楚这个过程，一定要在纸上画图。


以每根棒子的高度为矩形高度的方法中，每换一根棒子，都要向左、右遍历一遍，这样就做了重复工作。
其实可以在向左、右遍历的过程中 把这些棒子的高度记录下来，就不用重复了。
但具体记录什么信息呢？只记录高度是不够的，因为计算矩形面积还需要计算宽度，而宽度是由下标确定的。记录了
下标其对应的高度就可以直接从输入数组中得出。

比如对于棒子k,它左边的棒子肯定都探测过了，如果存下来了，那它的左边界肯定能用O(1)找到。

维护一个递增栈，如果新加入的元素 更大，那就说明右边界还无法确定，直接入栈；
如果新加入的元素更小，说明右边界确定了。那就可以将栈中元素依次出栈，计算以其为高度的最大矩形面积。
且其左边界肯定是栈中它下面的那个棒子，因为它下面紧挨着的那个棒子肯定是它左边第一个比它短的棒子。
'''


class Solution:
    def largest_rectangle_area_bad(self, heights):
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            area = (right_i - left_i - 1) * heights[i]
            res = max(res, area)
        return res

    def largest_rectangle_area_good(self, heights):
        res = 0
        # 它相当于在输入数组最左边，它一定比数组里所有元素都小，所以他肯定不会出栈，因此栈
        stack = [-1]

        # 右边的[-1] 因为它一定比输入数组里任何一个元素小，它会让输入数组里的所有元素都弹出
        for i, h in enumerate(heights + [-1]):
            while stack[-1] >= 0 and h < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    # result = s.largest_rectangle_area_bad(heights)
    result = s.largest_rectangle_area_good(heights)
    print(result)

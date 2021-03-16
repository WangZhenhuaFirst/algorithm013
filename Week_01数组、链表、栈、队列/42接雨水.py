'''
https://leetcode-cn.com/problems/trapping-rain-water/

42. 接雨水（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）

思路：
1.按行求：整体思路就是求第i层的水。遍历每个位置，如果当前高度小于i，且两边有高度>=i的，说明这个
地方一定有水，水就可以加1

2.按列求：O(N^2)
求每一列的水，只需要关注当前列，及左边最高的墙，右边最高的墙就够了。
装水的多少，根据木桶效应，只需要看左边最高的墙和右边最高的墙中较矮的一个就够了。
- 较矮的墙 > 当前列，较矮的墙 - 当前列
- 较矮的墙 <= 当前列，存不了水

3.动态规划:按列求的方法中，对于每一列，求它左边最高的墙和右边最高的墙，都要重新遍历一遍所有墙，可以优化。
max_left[i] = max(max_left[i-1], height[i-1])
max_right[i] = max(max_right[i+1], height[i+1])



4.双指针


5.栈：本题和括号匹配类似。每次匹配出一对括号（找到对应的一堵墙)，就计算这两堵墙中的水。
我们用栈保存每堵墙。
遍历时，如果当前高度小于栈顶的墙高度，说明这里会有积水，将当前下标入栈。
如果当前高度大于栈顶的墙的高度，说明之前的积水到这里停下，我们可以计算之前有多少积水了。计算完，就
把当前的墙继续入栈，作为新的积水的墙。
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        '''按列求，时间 O(N^2)，空间O(1)'''
        if not height:
            return 0
        sum = 0
        # 最两端的列不用考虑，因为一定不会有水
        for i in range(1, len(height) - 1):
            max_left = 0
            # 找出左边最高的
            # 关键是这一句，height[j]不是要和height[i]比，而是要和max_left比,才能找到最大的
            for j in range(i-1, -1, -1):
                if height[j] > max_left:
                    max_left = height[j]

            max_right = 0
            # 找出右边最高的
            for j in range(i+1, len(height)):
                if height[j] > max_right:
                    max_right = height[j]

            # 找出两端较小的
            min_value = min(max_left, max_right)
            # 只有较小的一段大于当前列时，才会有水
            if min_value > height[i]:
                sum += min_value - height[i]
        return sum

    def trap(self, height: List[int]) -> int:
        '''动态规划,时间O(N)，空间O(N)'''
        if not height:
            return 0

        sum = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(1, n-1):
            # height[i-1]是随着i的增大，新加入进来的，或者说紧贴着i最左边的
            # max_left[i-1]则把之前左边最高的存起来了，是在用空间换时间
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        for i in range(1, n-1):
            min_value = min(max_left[i], max_right[i])
            if min_value > height[i]:
                sum += min_value - height[i]
        return sum

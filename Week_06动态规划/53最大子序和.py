'''
https://leetcode-cn.com/problems/maximum-subarray/

53. 最大子序和（亚马逊、字节跳动在半年内面试常考）

思路：
1.暴力：O(N^2)
2.动态规划：O(N)
最大子序和 = 当前元素自身最大 / 包含之前的和 后 最大
分治（子问题）: max_sum(i) = max(max_sum(i-1), 0) + a[i]
状态数组定义:f[i]
DP方程: f[i] = max(f[i-1], 0) + a[i]



容易想不明白的地方：最大和 不一定是正数，只是 矬子里拔将军。



'''


def maxSubArray(nums):
    dp = nums  # 直接让dp = nums, 更简洁
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return max(dp)

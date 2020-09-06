'''
https://leetcode-cn.com/problems/maximum-subarray/

53. 最大子序和

思路：
1.暴力：O(N^2)
2.动态规划：
最大子序和 = 当前元素自身最大 / 包含之前的和后最大
分治（子问题）: max_sum(i) = max(max_sum(i-1), 0) + a[i]
状态数组定义:f[i]
DP方程: f[i] = max(f[i-1], 0) + a[i]


'''


def maxSubArray(nums):
    dp = nums
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    return max(dp)

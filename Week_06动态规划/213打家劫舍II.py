'''
https://leetcode-cn.com/problems/house-robber-ii/description/

213. 打家劫舍II（字节跳动在半年内面试中考过）

思路：第一个和最后一个房子中 只能偷一个，因此可以转化为两个单排排列的子问题：
不偷第一个 nums[1:]
不偷最后一个 nums[:n-1]











'''


def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    def part(array):
        dp = [0] * (n-1)
        dp[0] = array[0]
        dp[1] = max(array[0], array[1])
        for i in range(2, len(array)):
            dp[i] = max(dp[i-1], dp[i-2] + array[i])
        return dp[-1]

    return max(part(nums[:n-1]), part(nums[1:]))


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def my_rob(nums):
        pre, cur = 0, 0
        for num in nums:
            pre, cur = cur, max(cur, pre + num)
        return cur
    return max(my_rob(nums[1:]), my_rob(nums[:-1]))

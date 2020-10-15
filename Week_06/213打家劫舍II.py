'''
https://leetcode-cn.com/problems/house-robber-ii/description/

213. 打家劫舍II（字节跳动在半年内面试中考过）

思路：第一个和最后一个房子中 只能偷一个，因此可以转化为两个单排排列的子问题：
不偷第一个 nums[1:]
不偷最后一个 nums[:n-1]











'''


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

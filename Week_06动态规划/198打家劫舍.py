'''
https://leetcode-cn.com/problems/house-robber/

198. 打家劫舍（字节跳动、谷歌、亚马逊在半年内面试中考过）

思路：
DP方程：DP数组也可以叫 子问题数组，因为数组中每个元素都对应一个子问题。

确定DP数组的 计算顺序：dp[i] = max(dp[i-1], nums[i] + dp[i-2])
dp[i]的计算依赖于 dp[i-1]和dp[i-2]，所以计算顺序应该是从小到大的。
这样计算dp[i]时，它所依赖的子问题已经计算出来了。



1.思考方式一：加一个维度，来表示是否偷第i个元素
dp[i][0/1]
0：不偷， 1：偷

dp[0][0] = 0
dp[0][1] = nums[0]

dp[i][0] = max(dp[i-1][0], dp[i-1][1])
dp[i][1] = dp[i-1][0] + nums[i]

2.另一种思考方式：dp中存的是到i为止的最大值
dp[i] = max(dp[i-1], nums[i] + dp[i-2])
如果不偷第i个，则取dp[i-1]；如果偷第i个，则取 nums[i] + dp[i-2]
dp[0] = nums[0] # 如果只考虑第一个，那肯定是偷 最大
dp[1] = max(nums[0], nums[1]) # 相邻的两个，只能偷其中一个

3.在2的基础上优化空间：

'''


def rob(nums: List[int]) -> int:
    '''加额外空间，同时保存i偷和不偷两种情况'''
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [[0]*2 for _ in range(n)]
    # base case
    dp[0][0] = 0  # 不偷第一个
    dp[0][1] = nums[0]  # 偷第一个
    for i in range(1, n):
        # 偷i或不偷i，这两种都保存起来
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0] + nums[i]
    return max(dp[n-1][0], dp[n-1][1])


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n  # dp中存的是 到i为止的最大值
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        # 如果不偷第i个房子，那么问题就变成在 前i-1个房子中偷的子问题
        # 如果偷第i个房子，那么第i-1个房子肯定就不能偷了，其它房子不受影响，那么问题就变成在 前i-2个房子中偷
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    return dp[-1]


def rob(nums: List[int]) -> int:
    '''优化空间'''
    pre = 0
    now = 0
    for num in nums:
        # 循环开始时，now 表示dp[i-1], pre 表示dp[i-2]
        pre, now = now, max(now, num + pre)
        # 循环结束时，now 表示dp[i], pre表示dp[i-1]
    return now

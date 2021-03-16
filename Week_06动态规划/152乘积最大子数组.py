'''
https://leetcode-cn.com/problems/maximum-product-subarray/description/

152.乘积最大子数组（亚马逊、字节跳动、谷歌在半年内面试中考过）

思路：O(N)
令imax为当前最大值，则 imax = max(imax * nums[i], nums[i])

由于存在负数，会导致 最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin
imin = min(imin * nums[i], nums[i])

当负数出现时 imax 和 imin 互换，再进行计算







'''


def maxProduct(nums: List[int]) -> int:
    max_value = float('-inf')
    imax = 1
    imin = 1
    for i in range(len(nums)):
        if nums[i] < 0:
            imax, imin = imin, imax
        imax = max(imax * nums[i], nums[i])
        imin = min(imin * nums[i], nums[i])
        max_value = max(max_value, imax)  # max_value存的是所有可能的最大值中 最大的那个
    return max_value

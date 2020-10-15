'''
https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/

153. 寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）

https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/tong-guo-hua-tu-geng-neng-shen-ke-li-jie-er-fen-fa/
此题画图最好理解：
目标就是寻找数组中第一个小于 nums[end] 的数字。
为什么不能是第一个小于nums[start]的数字呢？因为当整个数组没有旋转过，单调递增时，就没有比nums[start]更小的数字了。









'''


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:  # 说明旋转的点在 mid 右边
                left = mid + 1
            else:
                right = mid  # 最小值有可能就是mid本身，所以这里不减一
        return nums[left]

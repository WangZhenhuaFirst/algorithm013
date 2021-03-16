'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

26. 删除排序数组中的重复项（Facebook、字节跳动、微软在半年内面试中考过）

思路：
双指针：O(n)
注意数组是有序的，那么重复的元素一定相邻。
要求删除重复元素，实际上就是将不重复的元素 移动到数组左侧。
用两个指针i和j,比较nums[i]和nums[j] 是否相等，
如果相等，j后移一位，
如果不相等，将j位置的元素复制到i+1位置上，i后移一位，j后移一位
重复上述过程，直到j等于数组长度
返回i+1，即为新数组长度





'''


class Solution:
    def remove_duplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

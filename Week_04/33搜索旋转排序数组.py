'''
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

33. 搜索旋转排序数组

1.暴力遍历，直接找目标元素：O(N)

2.找到乱序的地方，还原排序 O(N)/O(logN) ————二分查找 ???
3.直接二分查找:
单调：其实整个数组大部分都是有序的，只是在旋转点那个地方大小反过来了而已
边界
index

将待搜索区间一分为二，mid 一定会落在其中一个有序区间里。
还可以这样理解：中间元素mid 把待搜索区间分成了两部分，两部分中至少有一部分是有序的。



'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:  # while 循环中有等于判断
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 为什么nums中没有重复元素，但还是要 <= ，而不是 <  ?
            # Since when there's only two elements, the mid and low points to
            # exactly the same element. Then you have to include = to make sure
            # it covers this situation
            if nums[left] <= nums[mid]:  # 说明左半边是有序的
                # 因为此时左半边是有序的，所以左半边的if条件好写
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

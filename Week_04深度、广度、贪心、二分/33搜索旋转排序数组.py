'''
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

33. 搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）

思路：
1.暴力遍历，直接找目标元素：O(N)

2.找到乱序的地方，还原排序 O(N)/O(logN) ————二分查找 ???
3.直接二分查找:
单调：其实整个数组 大部分都是有序的，只是在旋转点那个地方 大小反过来了而已
边界
index

中间元素mid 把待搜索区间 分成了两部分，两部分中 至少有一部分是有序的。




'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''暴力, O(N)'''
        for num in nums:
            if num == target:
                return nums.index(num)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        '''二分查找 O(log(N))'''
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
            # 也就是整个数组nums只有两个元素时，left 其实等于mid
            if nums[left] <= nums[mid]:  # 说明左半边是有序的
                # 因为此时左半边是有序的，所以左半边的if条件好写
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 说明右半边是有序的
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

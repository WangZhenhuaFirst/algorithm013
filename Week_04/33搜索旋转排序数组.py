'''
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

33. 搜索旋转排序数组

1.暴力遍历，直接找目标元素：O(N)

2.找到乱序的地方，还原排序 O(N)/O(logN) ————二分查找
3.直接二分查找:
单调：其实整个数组大部分都是有序的，只是在旋转点那个地方大小反过来了而已
边界
index
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

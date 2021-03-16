'''
https://leetcode-cn.com/problems/merge-sorted-array/

88. 合并两个有序数组（Facebook 在半年内面试常考）

思路：













'''


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    '''O(m + n)'''
    # 双指针，从后往前
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1  # p用于追踪添加元素的位置
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    # 当p1 == -1，如果nums2中还有元素没遍历到，直接把 nums2中还没遍历到的元素copy到nums1中
    nums1[:p2+1] = nums2[:p2+1]

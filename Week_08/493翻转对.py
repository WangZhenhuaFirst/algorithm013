'''
https://leetcode-cn.com/problems/reverse-pairs/

493. 翻转对（字节跳动在半年内面试中考过）

思路：逆序对问题，

1.嵌套循环 O(N^2)
2.merge-sort: 将数组一分为二，如果左边区间的当前元素 > 右边区间一个元素的两倍，因为左边、右边
区间都已经排好序，都是递增的，所以左边区间剩下的元素都满足条件，不用再遍历了。




'''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0
        mid = left + (right - left) // 2
        cnt = self.mergeSort(nums, left, mid) + \
            self.mergeSort(nums, mid + 1, right)
        cache = [0] * (right - left + 1)
        i, t, c = left, left, 0
        for j in range(mid + 1, right + 1):
            while t <= mid and nums[t] / 2 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            # 因为左右都是递增的，nums[t]/2 > nums[j]，则 t 和 mid 之间的都满足条件
            cnt += mid - t + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[left:right + 1] = cache
        return cnt

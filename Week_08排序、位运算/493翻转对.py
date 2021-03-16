'''
https://leetcode-cn.com/problems/reverse-pairs/

493. 翻转对（字节跳动在半年内面试中考过）

思路：逆序对问题
1.嵌套循环 O(N^2)
2.merge-sort: 将数组一分为二，如果左边区间的当前元素 > 右边区间一个元素的两倍，因为左边、右边
区间 都已经排好序，都是递增的，所以左边区间剩下的元素 都满足条件，就不用再遍历了。









'''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if left >= right:  # 递归终止条件
            return 0

        mid = left + (right - left) // 2
        count = self.mergeSort(nums, left, mid) + \
            self.mergeSort(nums, mid + 1, right)
        cache = [0] * (right - left + 1)

        # 注意，递归的每一层的left 和right，其数值都是不一样的，每一层的合并都在计算逆序对的个数
        # i 和 t 初始值都是left，但 i是用来合并左右部分的，t是用来计算反转对的
        i, t, c = left, left, 0
        for j in range(mid + 1, right + 1):
            while t <= mid and nums[t] / 2 <= nums[j]:  # 用除法可以防止数字太大溢出
                t += 1
            # 因为左右都是递增的，nums[t]/2 > nums[j]，则 t 和 mid 之间的都满足条件
            # 注意，这句是在for循环内部的，因为每个j都要将所有大于它的 计数一次
            count += mid - t + 1
            
            while i <= mid and nums[i] <= nums[j]:  # 这部分是用来merge的
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            
        # 如果上面的while中有一个nums[i] > nums[j]，因为左右都是递增的，则后面的nums[i] 都会 > nums[j]
        # 所以只会剩下nums[i],不会剩下nums[j]
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[left:right + 1] = cache
        return count

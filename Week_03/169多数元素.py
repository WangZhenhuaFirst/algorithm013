'''
https://leetcode-cn.com/problems/majority-element/description/

169. 多数元素（亚马逊、字节跳动、Facebook 在半年内面试中考过）

思路：
1.暴力：O(N^2),枚举数组中的每个元素，再遍历一遍数组统计其出现次数













'''


class Solution:
    def majorityElement(self, nums):
        '''哈希表:O(N), 键表示一个元素，值表示该元素出现的次数'''
        num_hash = {}
        for num in nums:
            num_hash[num] = num_hash.get(num, 0) + 1
            if num_hash[num] > len(nums)/2:
                return num

    def majorityElementSort(self, nums):
        '''
        排序：O(NlogN),排序后，下标为n/2的元素一定是众数
        因为众数的个数>n/2，所以排序后中间的那个数一定是众数
        '''
        nums.sort()
        return nums[len(nums)//2]

    def majorityElementVote(self, nums):
        '''
        Boyer-Moore摩尔投票算法：O(N)，如果把众数记为 +1，
        把其他数记为 -1，将它们全部加起来，显然和大于 0
        '''
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

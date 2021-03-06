'''
https://leetcode-cn.com/problems/3sum/

15. 三数之和（国内、国际大厂历年面试高频老题）

思路：
1.返回 不重复的 三元组
2.可能不存在，此时应返回空数组
3.数组内如果有重复数字，结果可能会重复


1.暴力求解，三重循环：O(n^3)

2.两重暴力循环 + hash：O(n^2)

3.夹逼/双指针：O(N^2)，其中固定指针k循环复杂度O(N)，双指针i、j复杂度O(N)

'''


class Solution:
    def three_sum_bad(self, nums):
        '''三重循环,时间复杂度太高'''
        n = len(nums)
        if n < 3:
            return []
        # 为了方便去重，先排个序
        nums.sort()
        result = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        # 没找到好的去重方式 ???
        # set的key必须是不可变的,直接set(result)会报错：TypeError: unhashable type: 'list'
        # 将result的元素都转为tuple,用tuple做key,然后用set 去重。再将每个元素和列表转为list

        # 拼接字符串作为set的key也是一种方法
        return [list(t) for t in set(tuple(_) for _ in result)]

    def three_sum_good(self, nums):
        n = len(nums)
        if n < 3:
            return []
        nums.sort()  # 因为返回结果不需要下标，可以排序后夹逼(nums排序复杂度为O(NlogN))
        res = []
        # 固定3个指针中最左(最小)数字的指针k，双指针i、j 分设在剩余数组两端
        for k in range(n-2):
            # 1.当nums[k] > 0 时直接break跳出，因为不可能有答案了
            if nums[k] > 0:
                break
            # 2.当k > 0 且 nums[k] == nums[k-1] 时 即跳过nums[k]，因为数组是排序过的，所以本次
            # 双指针搜索只会得到重复组合。因为当nums[k] == nums[k-1]时，nums[k]能得到的组合肯定都在nums[k-1]中出现过了。
            # 并且nums[k-1]能得到的组合只可能比nums[k]多，不会比它少
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = n - 1
            # 3.在i < j 的情况下，计算 s = nums[k] + nums[i] + nums[j]
            # 当s < 0, i += 1 并跳过所有重复的nums[i]
            # 当s > 0, j -= 1 并跳过所有重复的nums[j]
            # 当s = 0, 记录组合[k, i, j]，执行i += 1和j -= 1 并跳过所有重复的nums[i]和nums[j]
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        # 因为一开始就排序了，i、j 又会跳过所有重复的数值，所以就不需要再去重了
        return res

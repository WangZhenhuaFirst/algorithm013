'''
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


审题：
1.返回 不重复的 三元组
2.可能不存在，此时应返回空数组
3.数组内如果有重复数字，结果可能会重复

解题思路：
1.暴力求解，三重循环：O(n^3)

2.两重暴力循环 + hash：O(n^2) 学完哈希再写

3.夹逼/双指针：O(N^2)，其中固定指针k循环复杂度O(N)，双指针i、j复杂度O(N)
因为不需要下标，可以排序后夹逼(nums排序复杂度为O(NlogN))

固定3个指针中最左(最小)数字的指针k，双指针i、j 分设在剩余数组两端
1.当nums[k] > 0 时直接break跳出，因为不可能有答案了
2.当k > 0 且 nums[k] == nums[k -1] 时即跳过nums[k]，因为已经将nums[k-1]的所有组合加入
结果中，本次 双指针搜索只会得到重复组合(当nums[k]==nums[k-1]时，nums[k]能得到的组合肯定都在nums[k-1]中出现过了)
3.在i < j 的情况下，计算 s = nums[k] + nums[i] + nums[j]
  当s < 0,i+=1 并跳过所有重复的nums[i]
  当s > 0,j-=1 并跳过所有重复的nums[j]
  当s = 0,记录组合[k,i,j]，执行i+=1和j-=1 并跳过所有重复的nums[i]和nums[j]
'''


class Solution:
    def three_sum_bad(self, nums):
        '''时间复杂度太高'''
        if not nums or len(nums) <= 2:
            return []
        nums.sort()
        result = []
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        answer = [nums[i], nums[j], nums[k]]
                        result.append(answer)
        # 没找到好的去重方式
        new_result = [list(t) for t in set(tuple(_) for _ in result)]
        return new_result

    def three_sum_good(self, nums):
        nums.sort()
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
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
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = s.three_sum_good(nums)
    print(result)

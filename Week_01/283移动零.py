'''
https://leetcode-cn.com/problems/move-zeroes/

283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0, 1, 0, 3, 12]
输出: [1, 3, 12, 0, 0]

说明:
1.必须在原数组上操作，不能拷贝额外的数组。
2.尽量减少操作次数。

解题思路：
1. 开个新数组，遇到非零往数组前面放，遇到0往数组后面放（这种方法本题目不允许使用）

2. 两次遍历：O(N)，第一次遍历时，每遇到一个非0元素就将其往数组左边挪，第一次遍历完，j指针就指向了最后一个非0元素。
第二次遍历时，起始位置就从j开始到结束，将剩下的元素都置零

3. 一次遍历：O(N)，在原数组内进行index操作，一次遍历。
参考快速排序的思想，把0当做中间点，把不等于0的放到中间点的左边，等于0的放到其右边。
用两个索引，其中j用来存储非零元素的索引(j其实就是那个中间点，就是第一个0所在的位置)，i用来遍历数组。
遇到0不动，遇到非0时与j交换，正好是把0放到右边了，把非0挨个放到左边了。
而0虽然不是挨个放的，但所有的0元素都是一样的，不影响
'''


class Solution:
    def move_zeroes_twice(self, nums):
        j = 0
        # 第一次遍历先把非零元素挑出来，挨个放到前面
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

    def move_zeroes_once(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.move_zeroes(nums)
    print(nums)

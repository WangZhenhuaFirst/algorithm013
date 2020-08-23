'''
https://leetcode-cn.com/problems/jump-game/

55. 跳跃游戏

思路：
1.贪心：O(N)





'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''从前往后跳'''
        if not nums:
            return False
        max_reach = 0  # 初始化当前能到达的最远位置为0
        for i, num in enumerate(nums):
            if max_reach < i:
                return False
            if max_reach >= len(nums) - 1:
                return True
            max_reach = max(max_reach, i + num)

    def canJump(self, nums: List[int]) -> bool:
        '''从后往前推'''
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

'''
https://leetcode-cn.com/problems/jump-game/

55. 跳跃游戏（亚马逊、华为、Facebook 在半年内面试中考过）

思路：贪心：O(N)












'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        从前往后跳
        如果某一个作为起跳点的格子可以跳跃的距离是3，表示后面3个格子 都可以作为起跳点。
        '''
        if not nums:
            return False
        max_reach = 0  # 初始化当前能到达的最远位置为0
        for i, num in enumerate(nums):
            if max_reach >= len(nums) - 1:
                return True
            if max_reach < i:  # 如果连当前索引都没跳到，就不用再看下去了
                return False
            # i + num 就是从当前索引位置能跳到的最大位置
            # 把每一个能作为起跳点的格子 都尝试跳一次，把 能跳到的最远距离 不断更新
            max_reach = max(max_reach, i + num)

    def canJump(self, nums: List[int]) -> bool:
        '''从后往前推'''
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # 注意，只有满足if的条件，才执行 goal = i
            # 也就是说，是允许中间某个位置 不能跳到 后面的位置的，比如某些位置值为0
            # 因为每个元素代表 可以跳跃的最大长度，所以是 >= ，而不只是 =
            if i + nums[i] >= goal:
                goal = i
        return not goal

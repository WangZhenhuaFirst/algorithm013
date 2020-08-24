'''
https://leetcode-cn.com/problems/jump-game-ii/

45. 跳跃游戏 II

思路：
1.贪心算法：O(N) 找能跳的最远的
如果某一个作为起跳点的格子可以跳跃的距离是3，那么表示后面3个格子都可以作为起跳点。
对每一个能作为起跳点的格子都尝试一遍，把能跳到的最远距离不断更新。








'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_position = 0  # 记录目前能/已经跳到的最远位置
        end = 0  # 记录这次/已经跳跃的边界，到达边界step就+1
        step = 0
        # 注意：是len(nums) - 1，因为最后一次跳跃就到达最后一个位置了
        for i in range(len(nums) - 1):
            # 看在上一步已经能跳到的范围里，从哪个点再次跳跃能跳的最远
            max_position = max(max_position, i + nums[i])

            if i == end:  # 到达边界
                step += 1  # 再次起跳
                end = max_position  # 更新边界
        return step

'''
https://leetcode-cn.com/problems/jump-game-ii/

45. 跳跃游戏II （亚马逊、华为、字节跳动在半年内面试中考过）

思路：贪心算法 O(N) 
1.如果某一个作为起跳点的格子可以跳跃的距离是3，那么表示后面3个格子都可以作为起跳点。
  对每一个能作为起跳点的格子 都尝试一遍，把能跳到的最远距离 不断更新。
2.如果从这个起跳点 起跳叫做第1次跳跃，那从后面3个格子起跳都可以叫做第2次跳跃
3.









'''


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_position = 0  # 记录目前能跳到的最远位置
        end = 0  # 记录已经跳跃的边界/最远处，到达边界step就+1
        step = 0
        # 注意：是len(nums) - 1，因为从倒数第二个位置再一次跳跃就到达最后一个位置了
        # 如果从倒数第一个位置再跳一次就出界了
        for i in range(len(nums) - 1):
            # 看在上一步已经能跳到的范围里，从哪个点再次跳跃能跳的最远
            max_position = max(max_position, i + nums[i])

            # end 是要在 i 达到上次能跳到的最远位置的边界时 才更新的，
            # 而不是 max_position 到达 上次能跳到的最远位置 就更新
            # 在上次能跳到的最远位置 之内的 跳跃 都属于同一次跳跃，或者说 count 都不更新
            if i == end:  # 到达边界
                step += 1  # 再次起跳
                end = max_position  # 更新边界
        return step

'''
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。


解题思路：
对根节点来说，最大深度要么来自左子树，要么来自右子树，然后再递归下去即可

'''


class Solution:
    def max_depth(self, root):
        if not root:
            return 0
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

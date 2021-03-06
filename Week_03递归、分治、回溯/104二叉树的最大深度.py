'''
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

104. 二叉树的最大深度（亚马逊、微软、字节跳动在半年内面试中考过）



思路：对根节点来说，最大深度 要么来自左子树，要么来自右子树，然后再递归下去即可











'''


class Solution:
    def max_depth(self, root):
        if not root:  # 递归终止条件
            return 0
        # +1是加的本层，递归的每层都+1
        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

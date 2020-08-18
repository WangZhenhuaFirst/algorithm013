'''
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。


思路：
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--25/
和104题类似，但又有不同。
当某个节点只有左孩子或只有右孩子时，这个节点不是叶子节点。
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/di-gui-fa-yan-du-you-xian-sou-suo-python-by-juncao/

1.深度优先搜索


2.广度优先搜索
'''


class Solution:
    def minDepth(self, root):
        '''深度优先'''
        if not root:
            return 0
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

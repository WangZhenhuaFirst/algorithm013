'''
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

111. 二叉树的最小深度（Facebook、字节跳动、谷歌在半年内面试中考过）

思路：
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--25/

https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/di-gui-fa-yan-du-you-xian-sou-suo-python-by-juncao/
和104题类似，但又有不同。
当某个节点只有左孩子或只有右孩子时，这个节点 不是叶子节点。

四个出口条件：
1.节点为None，返回0即可，表示并不增加深度
2.左子节点为空，返回右子节点的最小深度+1。为什么不返回0，因为此时这个节点不是叶子节点，还要考察右子树节点
3.右子节点为空，返回左子节点的最小深度+1。
4.左右子树都有节点，那么返回左右子树中的最小深度，并且+1




1.深度优先搜索


2.广度优先搜索


'''


class Solution:
    def minDepth(self, root):
        '''深度优先'''
        if not root:
            return 0
        # 如果某个节点没有左子节点或右子节点了，则应该找其最大的路径
        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

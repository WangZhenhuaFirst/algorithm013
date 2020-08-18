'''
https://leetcode-cn.com/problems/invert-binary-tree/description/

226. 翻转二叉树


思路：
此题核心在于遍历节点，只要能遍历到每一个节点，就能反转它的左右孩子，至于遍历方式反而不重要。
1.递归：O(N)，即深度优先遍历：前序、中序、后序都可以
2.迭代：O(N)，即广度优先遍历/层次遍历，需要额外的数据结构——队列，来存放临时遍历到的元素。








'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''前序遍历'''
        if not root:
            return None
        # 交换当前节点的左右子树
        root.left, root.right = root.right, root.left
        # 递归地交换当前节点的左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        '''中序遍历'''
        if not root:
            return None

        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        # 注意：这里的root.left 就是交换之前的root.right
        self.invertTree(root.left)
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        '''后序遍历'''
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree(self, root):
        '''迭代/层序遍历'''
        if not root:
            return None
        # 将节点逐层放入栈，再迭代处理栈中的元素
        stack = [root]
        while stack:
            # 每次从栈中拿一个节点，并交换这个节点的左右子树
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root

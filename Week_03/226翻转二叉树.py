'''
https://leetcode-cn.com/problems/invert-binary-tree/description/

226. 翻转二叉树 (谷歌、字节跳动、Facebook 在半年内面试中考过)


思路：此题核心在于遍历节点，只要能遍历到每一个节点，就能反转它的左右孩子，至于遍历方式反而不重要。
1.递归：O(N)，即深度优先遍历：前序、中序、后序都可以。做二叉树的题目，第一想到的应该是递归
2.迭代：O(N)，即广度优先遍历/层次遍历，需要额外的数据结构——队列，来存放临时遍历到的元素。











'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''前序遍历'''
        if not root:
            return None
        # 交换当前节点的左右子树
        # 这行代码是真正做出交换操作的
        # 递归只是帮助遍历整棵树的所有节点，把这行代码应用到所有节点上而已
        root.left, root.right = root.right, root.left
        # 递归地交换当前节点的左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        '''中序遍历'''
        if not root:
            return None

        # 先压栈，遍历到叶子结点了，叶子结点的左右子树都为null
        # 所以下一层递归 return None，然后就能执行交换了
        # 然后是不断从栈中取出节点，从下到上交换
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        # 注意：这里的root.left 就是交换之前的root.right
        # 所以，本体用中序遍历不好
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
            node = stack.pop(0)
            # 为什么判断过while stack 了，这里还要再判断 if node ???
            # 可能是因为stack += node.left, node.right 没判断 node.left 和 node.right 是否为空
            if node:
                node.left, node.right = node.right, node.left
                stack += [node.left, node.right]
        return root

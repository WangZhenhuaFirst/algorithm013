'''
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。


解题思路：
1.递归:

2.迭代:用栈模拟递归??? 没理解透彻？？？
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-xi-lie-1er-cha-shu-de-qian-xu-bian-li-p/
'''


class Solution:
    def preorder_traversal_recursion(self, root):
        res = []

        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

    def preorder_traversal_iteration(self, root):
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 要先压栈right，再压栈left，因为栈是后进先出的
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

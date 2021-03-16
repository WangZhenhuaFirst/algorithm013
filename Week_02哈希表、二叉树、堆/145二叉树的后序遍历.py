'''
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

145. 二叉树的后序遍历





普通的迭代法 后序遍历
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-die-dai-fa-by-da-da-m/


'''


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''递归'''
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        res = []
        postorder(root)
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''迭代:None标记'''
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                node = stack.pop()
                result.append(node.val)
            else:
                stack.append(node)         # 中
                stack.append(None)         # 标记已经访问过，还没处理
                if node.right:
                    stack.append(node.right)  # 右
                if node.left:
                    stack.append(node.left)  # 左
        return result

    def postorderTraversal(self, root):
        '''迭代：bool标记'''
        if not root:
            return []
        stack = [(root, False)]
        res = []
        while stack:
            cur, visit = stack.pop()
            if visit:
                res.append(cur.val)
            else:
                stack.append((cur, True))
                if cur.right:
                    stack.append((cur.right, False))
                if cur.left:
                    stack.append((cur.left, False))
        return res

    def postorderTraversal(self, root):
        '''

'''
https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/

590. N叉树的后序遍历






'''


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''递归'''
        res = []

        def helper(root):
            if root:
                children = root.children
                # 对于每个child，都做和root一样的处理，
                # 这就是递归的本意，也就是分解成子问题
                for child in children:
                    helper(child)
                res.append(root.val)
        helper(root)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        '''迭代'''
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            children = node.children
            # 按这样的顺序，取出来是 根-右-左，reverse之后正好是 左-右-根
            for child in children:
                stack.append(child)
        res.reverse()
        return res

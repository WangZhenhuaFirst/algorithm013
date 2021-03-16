'''
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/

589. N叉树的前序遍历





'''


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''递归'''
        def helper(node):
            if node:
                res.append(node.val)
                children = node.children
                for child in children:
                    helper(child)
        res = []
        helper(root)
        return res

    def preorder(self, root: 'Node') -> List[int]:
        '''迭代'''
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res

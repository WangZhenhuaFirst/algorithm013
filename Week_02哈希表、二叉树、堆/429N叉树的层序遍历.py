'''
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

429. N叉树的层序遍历

思路：













'''


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''广度优先搜索'''
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                queue.extend(node.children)
            res.append(level)
        return res

    def levelOrder(self, root):
        '''深度优先搜索'''
        if not root:
            return []

        def dfs(node, level):  # 用level来记录该节点所在的层
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                dfs(child, level+1)
        res = []
        dfs(root, 0)
        return res

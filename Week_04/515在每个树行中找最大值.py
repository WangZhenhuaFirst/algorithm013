'''
https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/

515. 在每个树行中找最大值（微软、亚马逊、Facebook 在半年内面试中考过）















'''


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        '''BFS 队列'''
        if not root:
            return []
        res = []
        q = [(root, 0)]
        while q:
            cur, level = q.pop(0)
            # res中还没有这一层的值时，append
            if level == len(res):
                res.append(cur.val)
            # res中有了这一层的值后，和这一层的其他值两两比较找出最大值
            res[level] = max(res[level], cur.val)

            # 找出下一层所有节点，加到队列中
            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))
        return res

    def largestValues(self, root: TreeNode) -> List[int]:
        '''DFS 递归'''
        if not root:
            return []
        hash_map = {}

        def dfs(node, depth):
            if not node:  # 递归终止条件
                return
            else:
                if depth not in hash_map:
                    hash_map[depth] = node.val
                else:
                    hash_map[depth] = max(node.val, hash_map[depth])
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)
        return [hash_map[i] for i in hash_map]

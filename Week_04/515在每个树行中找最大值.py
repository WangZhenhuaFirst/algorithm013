'''
https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/

515. 在每个树行中找最大值
您需要在二叉树的每一行中找到最大的值。





'''


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        '''BFS 队列'''
        if not root:
            return []
        result = []
        q = [(root, 0)]
        while q:
            cur, level = q.pop(0)
            # result中还没有这一层的值时，append
            if level == len(result):
                result.append(cur.val)
            # result中有了这一层的值后，和这一层的其他值两两比较找出最大值
            result[level] = max(result[level], cur.val)

            # 找出下一层所有节点，加到队列中
            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))
        return result

    def largestValues(self, root: TreeNode) -> List[int]:
        '''DFS 递归'''
        if not root:
            return []
        hashMap = {}

        def dfs(node, depth):
            if not node:
                return
            else:
                if depth not in hashMap:
                    hashMap[depth] = node.val
                else:
                    hashMap[depth] = max(node.val, hashMap[depth])
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 1)
        return [hashMap[i] for i in hashMap]

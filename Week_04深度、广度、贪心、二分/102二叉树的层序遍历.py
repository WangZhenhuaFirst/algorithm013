'''
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/%23/description/

102. 二叉树的层序遍历（字节跳动、亚马逊、微软在半年内面试中考过）

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
思路：
1.BFS：怎么给BFS遍历的结果 分层呢？
在每一层遍历开始前，先记录队列中的节点数量n，然后 一口气处理完 这一层的n个节点


2.DFS:并不是按照层访问的，但只要访问时知道每个节点 是哪一层的，访问时加到所在层的数组中即可。
所以，每次递归时 都需要带一个index，便是当前的层数。如果当前行对应的list不存在，就加一个空list进去。
题目要求每一层的节点都是从左到右遍历，因此递归时 也要先递归左子树，再递归右子树。



和429题类似

'''


class Solution:
    def levelOrder(self, root):
        '''BFS，
        每个点进队出队各一次，故渐进时间复杂度为O(N)'''
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 获取当前队列的长度，这个长度相当于当前这一层的节点个数
            level = []  # 每一层开始都重新定义一个临时空数组，才好操作
            for _ in range(len(queue)):
                cur = queue.pop(0)  # 题目要求从左到右
                level.append(cur.val)
                # 如果节点的左右子树不为空，也放入队列中
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # 将这一层的list加入最终返回结果中
            res.append(level)
        return res

    def levelOrder(self, root):
        '''DFS, O(N)'''
        if not root:
            return []

        def dfs(node, level):
            # 在每一层的一开始，插入一个空的list
            if len(res) == level:
                res.append([])

            res[level].append(node.val)
            # 递归的处理左子树、右子树，同时将层数level + 1
            # 先判断 节点 是否为空，再决定是否递归，这样下一层递归中
            # 就不用判断节点是否为空，可以直接append了
            # 并且也可以避免 res最后多加一个 [] 的问题
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        res = []
        dfs(root, 0)
        return res

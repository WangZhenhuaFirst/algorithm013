'''
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/%23/description/

102. 二叉树的层序遍历 （字节跳动、亚马逊、微软在半年内面试中考过）

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
思路：
1.BFS：怎么给BFS遍历的结果分层呢？在每一层遍历开始前，先记录队列中的节点数量n，然后一口气处理完这一层的n个节点



2.DFS:并不是按照层访问的，但只要访问时知道每个节点是哪一层的，访问时加到所在层的数组中即可。
所以，每次递归时都需要带一个index，便是当前的层数。如果当前行对应的list不存在，就加一个空list进去。
题目要求每一层的节点都是从左到右遍历，因此递归时也要先递归左子树，再递归右子树。






'''


class Solution:
    def levelOrder(self, root):
        '''BFS'''
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            # 获取当前队列的长度，这个长度相当于当前这一层的节点个数
            size = len(queue)
            tmp = []
            for _ in range(size):
                cur = queue.pop(0)  # 题目要求从左到右
                tmp.append(cur.val)
                # 如果节点的左右子树不为空，也放入队列中
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # 将这一层的list加入最终返回结果中
            res.append(tmp)
        return res

    def levelOrder(self, root):
        '''DFS'''
        if not root:
            return []
        res = []

        def dfs(root, index):
            # 在每一层的一开始，插入一个空的list
            if len(res) == index:
                res.append([])

            res[index].append(root.val)
            # 递归的处理左子树、右子树，同时将层数index + 1
            if root.left:
                dfs(root.left, index + 1)
            if root.right:
                dfs(root.right, index + 1)

        dfs(root, 0)
        return res

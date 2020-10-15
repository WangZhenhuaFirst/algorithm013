'''
https://leetcode-cn.com/problems/friend-circles/

547. 朋友圈（亚马逊、Facebook、字节跳动在半年内面试中考过）

思路：
1.DFS/BFS搜索，类似岛屿问题

2.并查集：解决图论中 动态连通性 问题。
并查集‘模型’是个多叉树，但其代码实现用的是数组，用数组来模拟出一个多叉树。










'''


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        DFS
        选择一个节点，访问其任一相邻的节点，看是否是连接，如果连接，再访问这一新的节点的任一相邻节点
        这样深度遍历下去，直到没有未访问的相邻节点时，就把这一块连在一起的节点都标记为已访问了，也只计数了1次

        再从头找一个新节点

        如果还没被放进visited，说明这个节点跟已经访问过的节点不相连，如果相连，肯定早就放进visited里了
        '''
        n = len(M)
        count = 0
        visited = set()

        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1  # 自己跟自己肯定是朋友
                visited.add(i)
                dfs(i)
        return count

    def findCircleNum(self, M: List[List[int]]) -> int:
        '''标准 并查集'''
        if not M:
            return 0
        n = len(M)
        p = [i for i in range(n)]

        def union(p, i, j):  # 抄模板即可
            p1 = self._parent(p, i)
            p2 = self._parent(p, j)
            p[p2] = p1

        def parent(p, i):  # 抄模板即可
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                i, p[i] = p[i], root
            return root

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    union(p, i, j)
        # 因为每个学生至少和自己是朋友，所以每个i都有自己的root，所以都能用_parent函数去计算
        return len(set([parent(p, i) for i in range(n)]))

    def findCircleNum(self, M: List[List[int]]) -> int:
        '''简化并查集'''
        def union(i, j):
            p[find(j)] = find(i)

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(i):  # 矩阵是按对角线对称的，所以只需要看一半
                if M[i][j] == 1:
                    union(i, j)  # 如果i和j是朋友，就把他们放到一个并查集中
        for i in range(n):
            find(i)
        return len(set(p))

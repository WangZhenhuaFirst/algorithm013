'''
https://leetcode-cn.com/problems/friend-circles/

547. 朋友圈

思路：
1.DFS/BFS 搜索， 类似岛屿问题

2.并查集








'''


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    union(i, j)
        for i in range(n):
            find(i)
        return len(set(p))

        def union(i, j):
            p[find(j)] = find(i)

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        n = len(M)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)

        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            x = p[i]
            p[x] = root
        return root

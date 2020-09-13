'''
https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/

1091. 二进制矩阵中的最短路径  （亚马逊、字节跳动、Facebook 在半年内面试中考过）

思路：
1.DP
2.BFS
3.A*:尽量往右下方向走，会最快。




'''

import heapq


def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    '''BFS'''
    n = len(grid)
    q = [(0, 0, 2)]  # 起点、终点、步数
    if grid[0][0] or grid[-1][-1]:
        return -1
    elif n <= 2:
        return n

    for i, j, d in q:
        for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                if x == n - 1 and y == n - 1:
                    return d
                q += [(x, y, d + 1)]
                grid[x][y] = 1  # 对已经走过的格子做标记
    return -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''A*'''
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        elif n <= 2:
            return n

        def heuristic(x, y):
            return max(abs(n-1 - x), abs(n-1 - y))

        h = []
        heapq.heappush(h, (0, (0, 0, 2)))
        visited = set()
        while h:
            _, (i, j, step) = heapq.heappop(h)
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if x == n - 1 and y == n - 1:
                    return step
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    heapq.heappush(
                        h, (step + heuristic(x, y), (x, y, step+1)))
        return -1

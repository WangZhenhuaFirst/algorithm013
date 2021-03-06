'''
https://leetcode-cn.com/problems/number-of-islands/

200. 岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次）

思路：网格类问题，网格结构遍历 比二叉树复杂。

DFS模板：
```
def traverse(root):
    if not root:
        return
    traverse(root.left)
    traverse(root.right)
```
所以dfs有两个要素：访问相邻节点 + 判断base case
网格的dfs，完全可以参考二叉树的dfs。
首先，每个格子有多少相邻节点？上下左右4个，也可以说 网格是 四叉的
其次，网格中的base case是什么？或者说不需要再继续遍历的条件是什么？越界。这和二叉树的root == null 一回事
网格与二叉树DFS最大的不同是，可能会 重复遍历，因为 网格本质上是个图：可以把每个格子看成图中的点，每个节点有上下左右四条边。


从一个点 扩散开，找到与其连通的点，其实就是从一个点开始，进行一次深度或广度优先遍历。
嵌套循环：遇到1，岛屿数量加1，然后把与这个1相邻的1打掉,这时候就只能用递归了，因为实际上是要把
相邻和相邻的相邻、相邻的相邻的相邻 都打掉。
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''DFS O(MN)，其中 M 和 N 分别为行数和列数'''
        def dfs(i, j, m, n):
            marked[i][j] = True  # 因为每个1都要被标记为TRUE，所以这句放在这里
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j, m, n)

        # 方向数组，它表示了相对于当前位置的4个方向的 横、纵坐标的偏移量
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                # 没有访问过，且是陆地，就用dfs遍历与之相邻的陆地
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1  # 同一片陆地，只做一次计数
                    dfs(i, j, m, n)
        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        '''BFS, O(MN)，其中 M 和 N 分别为行数和列数'''
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = []
                    queue.append((i, j))
                    # 要在一个格子刚入队时就立即标记为已经访问，否则会重复入队
                    marked[i][j] = True
                    while queue:
                        cur_x, cur_y = queue.pop(0)
                        for direction in directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            # BFS与DFS的不同之处是 没用递归，而是借助一个队列，访问完一层之后，把下一层加到队列里，这样逐层访问下去
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True
        return count

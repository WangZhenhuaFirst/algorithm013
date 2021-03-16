'''
https://leetcode-cn.com/problems/surrounded-regions/

130. 被围绕的区域 （亚马逊、eBay、谷歌在半年内面试中考过）

思路：拿到基本就可以确定是图的DFS、BFS遍历的题目了。
边界上的O及与其联通的O要特殊处理，剩下的O替换成X即可。
问题转化为，如何寻找和边界联通的O。
寻找特殊的O时，不替换为X，而是先标记为 #，寻找完成后。重新遍历一遍，把 # 恢复为O，O替换为X

如何寻找和边界联通的O ？ 从边界出发，对图进行 DFS 和 BFS

1.DFS
2.BFS
DFS和BFS的区别是，DFS是一条道走到黑，直到无路可走，再走下一条路；BFS是 一层层地走，走完一层 再走下一层

3.并查集


'''


def solve(self, board: List[List[str]]) -> None:
    '''DFS'''
    # not board就是防止 None
    # board[0]取到的是第一行，not board[0] 是为了避免输入是[]，len(board[0])取不到第一行会报错
    if not board or not board[0]:
        return
    row = len(board)
    col = len(board[0])

    def dfs(i, j):
        board[i][j] = '#'
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_i = i + x
            next_j = j + y
            if 0 < next_i < row - 1 and 0 < next_j < col - 1 and board[next_i][next_j] == 'O':
                dfs(next_i, next_j)

    for j in range(col):
        if board[0][j] == 'O':  # 第一行
            dfs(0, j)
        if board[row-1][j] == 'O':  # 最后一行
            dfs(row-1, j)
    for i in range(row):
        if board[i][0] == 'O':  # 第一列
            dfs(i, 0)
        if board[i][col-1] == 'O':  # 最后一列
            dfs(i, col-1)

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == '#':
                board[i][j] = 'O'


def solve(self, board: List[List[str]]) -> None:
    '''BFS'''
    if not board or not board[0]:
        return
    row = len(board)
    col = len(board[0])

    def bfs(i, j):
        queue = []
        queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            if 0 <= i < row and 0 <= j < col and board[i][j] == 'O':
                board[i][j] = '#'
                for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    queue.append((i+x, j + y))

    for j in range(col):
        if board[0][j] == 'O':
            bfs(0, j)
        if board[row-1][j] == 'O':
            bfs(row-1, j)

    for i in range(row):
        if board[i][0] == 'O':
            bfs(i, 0)
        if board[i][col-1] == 'O':
            bfs(i, col-1)

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == '#':
                board[i][j] = 'O'


def solve(self, board: List[List[str]]) -> None:
    '''并查集'''

    if not board or not board[0]:
        return
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':

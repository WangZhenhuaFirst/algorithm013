'''
https://leetcode-cn.com/problems/sliding-puzzle/

773. 滑动谜题 (微软、谷歌、Facebook 在半年内面试中考过）

思路：
1.DFS
2.BFS
3.A*



'''


from collections import namedtuple


def slidingPuzzle(self, board: List[List[int]]) -> int:
    '''BFS'''
    # 类似四联通，是每个索引位置可以交换的位置
    moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }
    used = set()
    s = "".join(str(c) for row in board for c in row)
    count = 0
    q = [s]
    while q:
        new = []
        for s in q:
            if s == "123450":
                return count
            used.add(s)
            arr = [c for c in s]  # 重新打碎

            # 开始移动0
            zero_index = s.index('0')
            for move in moves[zero_index]:
                new_arr = arr[:]
                new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]
                new_s = ''.join(new_arr)
                if new_s not in used:
                    new.append(new_s)
        count += 1
        q = new
    return -1


def slidingPuzzle(board):
    '''BFS'''
    def swap(s, i, j):
        if i < j:
            return s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
        else:
            return s[:j]+s[i]+s[j+1:i]+s[j]+s[i+1:]

    moves = {
        0: {1, 3},
        1: {0, 2, 4},
        2: {1, 5},
        3: {0, 4},
        4: {1, 3, 5},
        5: {2, 4}
    }
    used = set()
    s = ''.join(map(str, sum(board, [])))
    q = [(s.index('0'), s, 0)]
    # i is index of "0",
    # s is board state string
    # k is number of moves
    for i, s, k in q:
        if s == '123450':
            return k
        used.add(s)

        for j in moves[i]:
            for ns in {swap(s, i, j)}:
                if ns not in used:
                    q += [(j, ns, k+1)]
    return -1


# def slidingPuzzle(self, board: List[List[int]]) -> int:
#     '''A*'''
#     self.scores = [0] * 6
#     goal_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
#                 4: (1, 0), 5: (1, 1), 0: (1, 2)}

#     for num in range(6):
#         self.socres[num] = [[abs(goal_pos[num][0] - i) + abs(goal_pos[num][1] - j)
#                              for j in range(3)] for i in range(2)]

#     Node = namedtuple('Node', ['heuristic_score', 'distance', 'board'])
#     heap = [Node(0, 0, board)]
#     closed = []

#     while len(heap) > 0:
#         node = heapq.heappop(heap)
#         if self.get_score(node.board) == 0:
#             return node.distance
#         elif node.board in closed:
#             continue
#         else:
#             for neighbor in self.get_neighbors(node.board):
#                 if neighbor in closed:
#                     continue
#                 heapq.heappush(heap, Node(
#                     node.distance + 1 + self.get_score(neighbor), node.distance + 1, neighbor))
#         closed.append(node.board)
#     return -1

#     def get_neighbors(self, board):
#         r, c = (0, board[0].index(0)) if 0 in board[0] else (
#             1, board[1].index(0))
#         res = []

#         for offr, offc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#             if 0 <= r + offr < 2 and 0 <= c + offc < 3:
#                 board1 = copy.deepcopy(board)
#                 board1[r][c], board1[r+offr][c +
#                                              offc] = board1[r+offr][c+offc], board[r][c]
#                 res.append(board1)
#         return res

#     def get_score(self, board):
#         return sum([self.scores[board[i][j]][i][j] for i in range(2) for j in range(3)])

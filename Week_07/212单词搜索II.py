'''
https://leetcode-cn.com/problems/word-search-ii/

212. 单词搜索 II

思路：
1. 遍历words --> board search O(N*M*M*4^k),N为words中的单词数，M为board的长、宽，k为单词的长度

2.Trie 
all words --> Trie构建起 prefix
board， DFS

思路1的想法： 从words中依次选定一个单词——> 从board中的每个位置出发，看能否组成这个单词
其实可以倒过来：从board中的每个位置出发——> 看遍历过程中是否遇到了 words 中的某个单词
可以事先把所有单词存到前缀树中。如果当前走的路径不是前缀树中的前缀，就可以提前结束了。如果是前缀树
中的单词，就将其存到结果中。


'''


def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # 构造字典树
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node['#'] = True

    def search(i, j, node, pre, visited):
        # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
        if '#' in node:
            res.add(pre)
        for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            _i, _j = i + di, j + dj
            if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited:
                search(_i, _j, node[board[_i][_j]], pre +
                       board[_i][_j], visited | {(_i, _j)})

    res, h, w = set(), len(board), len(board[0])
    for i in range(h):
        for j in range(w):
            if board[i][j] in trie:
                search(i, j, trie[board[i][j]],
                       board[i][j], {(i, j)})  # DFS搜索
    return list(res)

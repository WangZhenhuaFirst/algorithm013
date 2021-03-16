'''
https://leetcode-cn.com/problems/word-ladder-ii/description/

126. 单词接龙II （微软、亚马逊、Facebook 在半年内面试中考过）

思路：BFS，从起始节点开始遍历，如果找到了结束节点，代表找到了结果，同时这个肯定是最优解（路径最短）。
注意：此时并不能直接返回答案，因为要求的是 所有最短路径，所以我们要把这一层的所有满足结果都返回。












'''

import string


def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    '''单向BFS'''
    wordList = set(wordList)
    if endWord not in wordList:
        return []

    def edges(word):
        edges = []
        for i, v in enumerate(word):
            for c in string.ascii_lowercase:
                if c != v:
                    new = word[:i] + c + word[i+1:]
                    if new in wordList and new not in marked:
                        edges.append(new)
        return edges

    res = []
    marked = set()
    queue = [[beginWord]]  # 记录的直接就是一条条完整的路径
    while queue:
        tmp = []
        found = False
        for words in queue:  # words 就是一个个数组，也就是一条条路径
            marked.add(words[-1])
        for words in queue:
            for w in edges(words[-1]):  # 对于找到的每种 邻居，都形成一条新的path
                v = words + [w]
                if w == endWord:
                    res.append(v)
                    found = True
                    # 只要第一次找打了，就将found赋值为TRUE，因为BFS先找到的肯定是最短路径，且这一层都会在这个for循环里遍历完
                tmp.append(v)
        if found:  # 找到就不再遍历了，即使再有endWord，路径也会更长
            break
        queue = tmp
    return res


def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    '''双向BFS'''
    if endWord not in wordList:
        return []

    
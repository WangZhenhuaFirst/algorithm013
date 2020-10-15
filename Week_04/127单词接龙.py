'''
https://leetcode-cn.com/problems/word-ladder/description/

127. 单词接龙 （亚马逊、Facebook、谷歌在半年内面试中考过）

思路：无向图中两个顶点之间的 最短路径的长度，可以通过 BFS广度优先遍历得到
1.BFS
2.DFS
3.Two-ended BFS

每次转换只能改变一个字母。
每一次迭代中如何来找当前单词的转换单词呢？
这里面所用的方法有很多种，网上的帖子，大致分为两种。
一种是将改变的字母按照小写字母排列情况分为26种情况，依次填进去进行判断。
另一种是将改变字母的那个位置用“_”代替，比如“hit”要改变第二个位置的字母，则可表示为“h_t”，
而“hot”改变第二个位置的字母后也可表示为“h_t”，说明这两个单词是可以直接转换的。



'''

import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''BFS'''
        if endWord not in wordList:
            return 0

        front = {beginWord}
        dist = 1  # 要求的是转换序列的长度，所以一开始就是1，也就是beginWord也算一个
        wordList = set(wordList)
        word_len = len(beginWord)

        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word == endWord:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)  # 防止重复访问
            front = next_front  # 将front队列中的元素取空了，再将下一层的元素放到front中
        return 0  # 默认是return 0 的

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''双向BFS'''
        if endWord not in wordList:
            return 0

        front = {beginWord}
        back = {endWord}
        dist = 1  # 因为要求的是转换序列，而不是步数，所以一开始就初始化为1，而不是0
        wordList = set(wordList)
        word_len = len(beginWord)

        # 如果其中一个集合中没有单词了，也就肯定无法变换了，肯定就走不到了
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:  # 'a' -> 'z'
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            # 如果两个if都不满足，直接跳过这个词
                            if new_word in back:
                                return dist
                            if new_word in wordList:  # 转换过程中的词必须是词典中的词
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            # 每次都让front取小的那个，这样循环可以少操作一些单词
            # 注意，这里是要互换，而不是单纯的front = back
            if len(back) < len(front):
                front, back = back, front
        return 0

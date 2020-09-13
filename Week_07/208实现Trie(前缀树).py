'''
https://leetcode-cn.com/problems/implement-trie-prefix-tree/

208. 实现 Trie (前缀树) （亚马逊、微软、谷歌在半年内面试中考过）

思路：
参考：https://shimo.im/docs/DP53Y6rOwN8MTCQH/read

https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/ben-zhi-shang-shi-zi-dian-an-zi-mu-die-dai-by-tuot/
#第一次insert，最后一个'e'存在结束'end'
apple: {
    'a': {
        'p': {
            'p': {
                'l': {
                    'e': {
                        'end': True
                    }
                }
            }
        }
    }
}
'''


class Trie:
    def __init__(self):
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        node = self.root
        # 每个字符是一个节点
        for char in word:
            node = node.setdefault(char, {})  # 字典迭代，node 是更深一层的字典
        node[self.end_of_word] = self.end_of_word  # 单词结束标志

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # 在str结尾处有'#'才证明插入过这个单词，否则只是其它单词有这个前缀
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

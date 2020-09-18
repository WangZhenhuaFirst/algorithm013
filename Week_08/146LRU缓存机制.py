'''
https://leetcode-cn.com/problems/lru-cache/#/

146. LRU缓存机制 （亚马逊、字节跳动、Facebook、微软在半年内面试中常考）

思路：
要实现的数据结构必要的条件：查找快、插入快、删除快，有顺序之分。
什么数据结构同时符合上述条件呢？
哈希表查找快，但数据无固定顺序；
链表有顺序之分，插入删除快，查找慢。
所以结合一下，形成一种新的数据结构:哈希链表。

[LRU Cache Python 代码示例](https://shimo.im/docs/CoyPAyXooGcDuLQo/read)






'''

import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()  # OrderedDict的Key会按照插入的顺序排列
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)  # 把之前位置的key+value取走扔掉
        self.dic[key] = v  # 然后把这对key+value 加到最前面
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:  # remain指剩下的容量
                self.remain -= 1
            else:
                # The popitem() method returns and removes a key,value pair.
                # The pairs are returned in LIFO order if last is true
                # FIFO order if false
                self.dic.popitem(last=False)  # remain是0，把最老的元素弹出去
        self.dic[key] = value

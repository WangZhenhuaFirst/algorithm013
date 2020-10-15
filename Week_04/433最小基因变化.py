'''
https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description

433. 最小基因变化（谷歌、Twitter、腾讯在半年内面试中考过）

思路：用广度优先搜索解决 状态图搜索问题。













'''


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        '''广度优先搜索：从左到右，或者说从开始到最后，对于每个碱基，探索其所有变化的可能性'''
        bank = set(bank)  # 转为set，in判断只需 O(1)时间
        if end not in bank:  # 目标不在bank中，直接返回-1
            return -1
        q = [(start, 0)]  # 初始节点以及当前步数
        change = {'A': 'TCG', 'T': 'ACG',
                  'C': 'ATG', 'G': 'ATC'}  # 每个碱基及对应的可变换碱基
        while q:
            node, step = q.pop(0)  # 注意，用pop(0)
            if node == end:
                return step
            for i, v in enumerate(node):
                for j in change[v]:  # 该碱基可以改变的方式
                    new = node[:i] + j + node[i+1:]
                    if new in bank:
                        q.append((new, step + 1))  # 入队，继续广度搜索
                        bank.remove(new)  # 避免重复遍历
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        '''双向广度优先'''
        bank = set(bank)
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        change = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        step = 0
        while start_set:
            step += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change[s]:
                        new = node[:i] + c + node[i+1:]
                        if new in end_set:
                            return step
                        if new in bank:  # 每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            # 每次判断正向是否比负向的元素更多。我们选择元素更小的那个继续更新
            # 把A变成B，和把B变成A，本质上用的步数是一样的
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1

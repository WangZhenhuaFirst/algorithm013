## 并查集
参考：https://segmentfault.com/a/1190000004023326

顾名思义，有“合并集合” 和 “查找集合中的元素” 这两种操作的关于数据结构的一种算法。

算法：
用集合中的某个元素来代表这个集合
一个集合内的所有元素组织成以 代表元 为根的树形结构




## 并查集代码模板

[并查集代码模板](https://shimo.im/docs/VtcxL0kyp04OBHak/read)

```
def init(p):
    # 相当于
    #for i in range(n):
    #    p[i] = i
    p = [i for i in range(n)]

def union(self, p, i, j):
    p1 = self.parent(p, i)
    p2 = self.parent(p, j)
    p[p1] = p2

def parent(self, p, i):
    root = i
    while p[root] != root:
        root = p[root]
    # 路径压缩
    while p[i] != i:
        x = i
        i = p[i]
        p[x] = root
    return root
```

## 启发式搜索代码模板
https://shimo.im/docs/8CzMlrcvbWwFXA8r/read

```
def AstarSearch(graph, start, end):
    pq = collections.priority_queue()
    pq.append([start])
    visited.add(start)

    while pq:
        node = pq.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
        pq.push(unvisited)
```

## 双向BFS模板

```
start_queue, end_queue, visited, setps = [start], [end], set(), 0
visited.add(start_queue)

while start_queue and end_queue:
    if len(start_queue) > len(end_queue):  # 比较 start_queue 和 end_queue, 使得 start_queue 始终为两者中的较短这样，这样可以减少遍历的次数
        start_queue, end_queue = end_queue, start_end

    for i in range(len(start_queue)):
        curr = start_queue.pop(0)

        for child in curr.children:
            if child in end_queue:
                return steps + 1
            if child in visited:
                continue
            visited.add(child)
            start_queue.append(child)
        steps += 1
    return 0
```
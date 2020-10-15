## Tire树/前缀树 代码模板
https://shimo.im/docs/DP53Y6rOwN8MTCQH/read








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
    p = [i for i in range(n)] # 每个元素都自己指向自己

def union(self, p, i, j):
    # 找到各自的root，然后让一个集合的root指向另一个集合的root
    p1 = self.parent(p, i)
    p2 = self.parent(p, j)
    p[p1] = p2

def parent(self, p, i):
    root = i
    while p[root] != root: # 如果root节点不指向自身，说明还不是根节点
        root = p[root] # 那就将其父节点赋值给root，直到找到根节点
    # 路径压缩，会把这条路径上所有元素都直接指向 根元素
    while p[i] != i:
        # 把p[i]赋值给i这个字母/变量，也就是把 父元素赋值给了 i,是为了下次while循环下个元素
        i, p[i] = p[i], root 
    return root
```

## 双向BFS模板

```
start_queue, end_queue, visited, steps = [start], [end], set(), 0
visited.add(start_queue)

while start_queue and end_queue:
    if len(start_queue) > len(end_queue):  # 比较 start_queue 和 end_queue, 使得 start_queue 始终为两者中的较短这样，这样可以减少遍历的次数
        start_queue, end_queue = end_queue, start_queue

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


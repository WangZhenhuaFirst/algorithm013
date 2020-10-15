这里讲的搜索，就是暴力搜索，就是把所有节点遍历一遍，没有智能的优化。

https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
在实际使用中，我们用 DFS 的时候远远多于 BFS。
如果使用 DFS/BFS 只是为了遍历一棵树、一张图上的所有结点的话，那么 DFS 和 BFS 的能力没什么差别，我们当然更倾向于更方便写、空间复杂度更低的 DFS 遍历。DFS遍历的代码比BFS简洁太多了，这是因为递归的方式隐含地使用了系统的 栈，我们不需要自己维护一个数据结构。
不过，某些使用场景是 DFS 做不到的，只能使用 BFS 遍历。这就是两个场景：「层序遍历」、「最短路径」。

广度优先遍历，需要程序员自己编写节点类，显式使用队列这个数据结构。
深度优先遍历，可以直接使用系统栈，在递归方法执行完成时，系统栈顶就把我们所需要的状态信息直接弹出，
而无需编写节点类和显示使用栈。

## DFS 深度优先

https://shimo.im/docs/UdY2UUKtliYXmk8t/read

``` 
# 二叉树递归写法
def dfs(node):
    if node in visited:
        return

    visited.add(node)

    # process current node
    dfs(node.left)
    dfs(node.right)
```

```
# 多叉树递归写法
visited = set()

def dfs(node, visited):
    # terminator,这部分不写其实也能达到同样的效果
    # 因为下面的for循环中，如果node在visited中，就不会再递归下去了
    if node in visited:
        return

    visited.add(node)

    # process current node here
    for next_node in node.children()
        if not next_node in visited:
            dfs(next node, visited)
```

```
# 非递归写法
def dfs(self, tree):
    if tree.root is None:
        return []
    
    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
```


## BFS 广度优先

https://shimo.im/docs/ZBghMEZWix0Lc2jQ/read

```
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = genearte_related_nodes(node)
        queue.push(nodes)
```


# 贪心算法

如果贪心算法能/适合解决这个问题，那么写出的代码的复杂度会很低，因为你每一步都选择最优解，也就
删掉了那些次忧解，相当于不用遍历了；因为贪心算法不保存之前的选择，也不能回溯。复杂度当然会很低。


## 二分查找模板

https://shimo.im/docs/xvIIfeEzWYEUdBPD/read

```
left = 0
right = len(array) - 1
while left <= right:
    mid = (left + right)/2
    if array[mid] == target:
        return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```


## 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

```
def find_disorder(nums):
    left = 0
    right = len(nums) - 1
    while left < right: # 这里不能加等号，防止后面的nums[mid+1]越界
        mid = left + (right - left) // 2
        # 如果左指针小于中间值，说明左边是有序的
        if nums[left] < nums[mid]:
            # 且中间指针右移一位 小于中间值，则这就是无序位置
            if nums[mid] > nums[mid+1]:
                return [mid, mid+1]
            # 否则更新左指针
            left = mid + 1
        else:
            if nums[mid] < nums[mid-1]:
                return [mid-1, mid]
            right = mid - 1
    return []
```

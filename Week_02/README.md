


## 哈希表
集合set其实是由哈希表实现的，set 和 哈希表的区别就是 set 只有 key，没有value。
因为哈希表的key是不能重复的，所以就可以实现set

## 树
链表是特殊的树，是每个节点只有一个next指针的树；
树是特殊的图，是没有环的图。
这是透过现象看本质，所有复杂的数据结构都是由简单的数据结构进化而来的。
其实从本质上讲，数据结构只有两种：数组、链表，其他复杂的数据结构都是在这个基础上组合而来的。


## 为什么需要树、图这样的数据结构呢？
只有一维的数据结构不可以吗？为什么需要二维的数据结构？
因为我们所在的世界就是有二维的、三维的事物，所以工程上肯定是有这种需要的。
比如斐波那契数列


## 树的定义
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```


## 树的遍历
为什么需要遍历？如果是一颗普通的树，其中的节点是无序的，那么要查找某个元素，就只能通过遍历。

数的结构导致它的遍历 适合用递归来实现，用循环则比较麻烦。

前序遍历：根-左-右
对于树中的任意节点来说，先打印这个节点，再打印它的 左子树，最后打印它的右子树
```
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
```

中序遍历：左-根-右
对于树中的任意节点来说，先打印它的左子树，再打印它本身，最后打印它的右子树。
```
def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)
```

后续遍历：左-右-根
对于树中的任意节点来说，先打印它的左子树，再打印它的右子树，最后打印这个节点本身。
```
def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```


前序、中序、后序遍历都属于深度优先搜索 DFS
层序遍历是广度优先搜索BFS

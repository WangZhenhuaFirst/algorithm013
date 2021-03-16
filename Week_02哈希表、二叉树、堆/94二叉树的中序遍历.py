'''
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

94. 二叉树的中序遍历（亚马逊、微软、字节跳动在半年内面试中考过）

思路：
1.递归：递归是函数自己调用自己，操作系统自动帮我们用栈1来保存了每个调用的函数，O(N)
2.迭代：用迭代模拟递归的调用过程，O(N)
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/dong-hua-yan-shi-94-er-cha-shu-de-zhong-xu-bian-li/

dfs(root.left)
    dfs(root.left)
        dfs(root.left)
            为null返回
        打印节点
        dfs(root.right)
            dfs(root.left)
                dfs(root.left)
                ......
递归的调用过程是不断往左边走，当左边走到头了，就打印节点，然后转向右边，然后继续我那个左边走
'''


def inoder_traversal(self, root: TreeNode):
    '''
    递归
    https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-xi-lie-1er-cha-shu-de-qian-xu-bian-li-p/
    之所以要再定义一个函数，是因为题目要求返回这个树的遍历结果???
    '''
    def inorder(node):
        if node:
            inorder(node.left)  # 这句代码会不断递归，直到递归完根节点的整个左子树
            res.append(node.val)
            inorder(node.right)
    res = []
    inorder(root)
    return res


def inorderTraversal(self, root: TreeNode) -> List[int]:
    '''迭代:None标记'''
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            node = stack.pop()
            result.append(node.val)
        else:
            if node.right:
                stack.append(node.right)
            stack.append(node)
            stack.append(None)  # 根节点访问/遍历过了，但还没有处理，需要标记一下
            if node.left:
                stack.append(node.left)
    return result


def inorderTraversal(self, root):
    '''迭代：bool标记'''
    if not root:
        return []
    stack = [(root, False)]
    res = []
    while stack:
        cur, visit = stack.pop()
        if visit:
            res.append(cur.val)
        else:
            if cur.right:
                stack.append((cur.right, False))
            stack.append((cur, True))
            if cur.left:
                stack.append((cur.left, False))
    return res


def inoder_traversal_iteratively(self, root):
    '''普通迭代'''
    # 递归中 左边走不下去了，就会返回（递归函数返回，回到上一层），对应到迭代中就是else分支
    res, stack = [], []
    # root 和 stack 不会同时为空，除非整个树遍历完了
    # 比如当左边 走不下去的时候，root就变成空了，但此时栈中还有元素，说明节点还没遍历完
    # 当根节点弹出后，栈为空了，但root不为空，说明还有节点没遍历完
    while stack or root:
        # 不断往左子树方向走，每走一次就将当前节点保存到栈中
        # 这是模拟递归的调用
        if root:
            stack.append(root)
            root = root.left
        # 当前节点为空，说明左边走到头了，也就是该根节点没有左节点，从栈中弹出根节点并保存
        # 打印根节点
        # 转向右节点，继续上面的过程
        else:
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
    return res

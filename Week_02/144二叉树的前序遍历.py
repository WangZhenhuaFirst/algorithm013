'''
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

144. 二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。


解题思路：
1.递归:递归重要的就是想清楚：你想做什么 + 什么时候停止(终止条件是什么？)
不要试图去想清楚具体的递归细节，只要知道自己想做什么，然后写代码/指令让电脑去做就可以了。
计算机都可能会溢出，用人脑去递归就是找死。




2.迭代:
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/dai-ma-sui-xiang-lu-chi-tou-qian-zhong-hou-xu-de-d/
为什么前中后序遍历迭代法不统一？
因为迭代的过程中，我们有两个操作:处理，即将元素放进result中；访问，遍历节点。
前序是 中左右，先访问的元素是中间节点，要处理的也是中间节点，所以才能写出相对简洁的代码。
中序是 左中右，先访问的是二叉树顶部的节点，然后一层层向下访问，直到树左面的最底部，再开始处理节点。
也就是处理顺序和访问顺序是不一致的。 所以，用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，
栈则用来处理节点上的元素。
怎么写出前中后序遍历 迭代法统一的写法？
将访问的节点放入栈中
将要处理的节点也放入栈中，但要做标记。也就是要处理的节点放入栈之后，紧接着放入一个空指针作为标记。


另一种标记方式：
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/xian-xu-zhong-xu-hou-xu-de-fei-di-gui-ban-ben-by-l/

二叉树中的任意一个节点，都有两个角色需要扮演：一个是作为值存储的角色，另一个是作为它所带领的子树的一个代表。
设置一个bool变量，来说明我当前拿到这个节点时，应该以一个值存储的角色对待它（TRUE）————直接打印值，
还是应该以一个子树的代表这种角色对待它（FALSE）————需要继续探索由它带领的子树。




最全总结：
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/python3-er-cha-shu-suo-you-bian-li-mo-ban-ji-zhi-s/
'''


class Solution:
    def preorder_traversal_recursion(self, root):
        '''递归'''
        res = []

        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        迭代：None标记
        完全模仿递归，不变一行。
        递归的本质就是压栈，压的当然是待执行的内容。
        '''
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:  # 空节点表示遇到了之前已经访问过的节点了，现在需要处理
                node = stack.pop()
                result.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)  # 右， 先入栈的最后访问
                if node.left:
                    stack.append(node.left)   # 左
                stack.append(node)            # 中
                stack.append(None)            # 作为已访问过的标记
        return result

    def preorderTraversal(self, root):
        '''迭代：用bool标记'''
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
                if cur.left:
                    stack.append((cur.left, False))
                stack.append((cur, True))
        return res

    def preorder_traversal_iteration(self, root):
        '''普通迭代'''
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 要先压栈right，再压栈left，因为栈是后进先出的
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

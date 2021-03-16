'''
https://leetcode-cn.com/problems/validate-binary-search-tree/

98. 验证二叉搜索树 （亚马逊、微软、Facebook 在半年内面试中考过）

思路
二叉搜索树：
不仅要比较 root.val > root.left.val 和 root.val < root.right.val，
还要保证：整个左子树所有节点的值 都小于根节点，整个右子树所有节点的值都大于根节点

1.递归：O(N)
空间复杂度O(N)，因为递归过程中 需要为每层递归函数分配栈空间，所以需要的额外空间 取决于递归的深度，
即二叉树的高度。最坏情况下二叉树为一条链，树的高度为N

2.中序遍历:
O(N) 二叉树的每个节点 最多被访问2次，因此时间复杂度为O(n)
二叉搜索树 中序遍历 得到的值构成的序列 一定是升序的

'''


class Solution:
    def is_valid_bst_recursion(self, root):
        '''递归，利用最大值最小值'''
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            # 因为二叉搜索树要满足的不只是一层左子节点小于，右子节点大于
            # 所以任何一层不满足，就可以返回最终的FALSE
            # 判断当前节点的值是否在界内
            if val <= lower or val >= upper:
                return False
            # 将当前节点的值 作为上界，对node.left进行递归
            if not helper(node.left, lower, val):
                return False
            # 将当前节点的值作为下界，对node.right进行递归
            if not helper(node.right, val, upper):
                return False

            return True  # 对于这一层，除了以上三种情况外，其他情况 都满足
        return helper(root)  # 因为最终的结果依赖于 helper方法的返回值，所以helper方法中各种情况下都必须有返回值

    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        res = []
        helper(root)
        return res == sorted(res) and len(set(res)) == len(res)

    def isValidBST(self, root: TreeNode) -> bool:
        '''用递归中序遍历'''
        self.pre = None

        def isBST(node):
            if not node:
                return True
            if not isBST(node.left):
                return False
            if self.pre and self.pre.val >= node.val:
                return False
            self.pre = node
            return isBST(node.right)
        return isBST(root)

    def is_valid_bst_inorder(self, root):
        '''用迭代中序遍历'''
        if not root:
            return True

        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)  # 注意，这里append的是root，不是root.val
                root = root.left
            root = stack.pop()

            # inorder 是中序遍历前一个节点的值
            if root.val <= inorder:  # 注意，这里是 <=，不是 <
                return False
            inorder = root.val
            root = root.right
        return True

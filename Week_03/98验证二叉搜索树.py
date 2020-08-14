'''
https://leetcode-cn.com/problems/validate-binary-search-tree/

98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数————当前节点的值是其左子树的上界
节点的右子树只包含大于当前节点的数————当前节点的值是其右子树的下界
所有左子树和右子树自身必须也是二叉搜索树。

解题思路
二叉搜索树：
不仅要比较 root.val > root.left.val 和 root.val < root.right.val，
还要保证：整个左子树所有节点的值都小于根节点，整个右子树所有节点的值都大于根节点

1.递归：O(N)
空间复杂度O(N)，因为递归过程中需要为每层递归函数分配栈空间，所以需要的额外空间取决于递归的深度，
即二叉树的高度。最坏情况下二叉树为一条链，树的高度为N

2.中序遍历:
O(N) 二叉树的每个节点最多被访问2次，因此时间复杂度为O(n)
二叉搜索树「中序遍历」得到的值构成的序列一定是升序的

'''


class Solution:
    def is_valid_bst_recursion(self, root):
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True

            val = root.val
            # 判断当前节点的值是否在界内
            if val <= lower or val >= upper:
                return False

            # 将当前节点的值作为上界，对root.left进行递归
            if not helper(root.left, lower, val):
                return False
            # 将当前节点的值作为下界，对root.right进行递归
            if not helper(root.right, val, upper):
                return False
            return True
        return helper(root)

    def is_valid_bst_inorder(self, root):
        if not root:
            return True

        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # inorder 是中序遍历前一个节点的值
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
